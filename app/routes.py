from flask import render_template, request, redirect, session, jsonify, send_file
from app import app
from app.utils.calorie_predictor import calculate_required_calories
from app.utils.food_database import FOOD_DATA
import io
import json

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['age'] = int(request.form['age'])
        session['gender'] = request.form['gender']
        session['height'] = float(request.form['height'])  # cm
        session['weight'] = float(request.form['weight'])  # kg
        session['activity_level'] = request.form['activity_level']

        session['burned'] = 0
        session['intake'] = 0
        session['food_history'] = []

        # ✅ Fix: correct parameter order
        session['required'] = calculate_required_calories(
            session['gender'],
            session['age'],
            session['weight'],
            session['height'],
            session['activity_level']
        )
        return redirect('/dashboard')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',
                           name=session.get('name'),
                           required=session.get('required'),
                           intake=session.get('intake', 0),
                           burned=session.get('burned', 0),
                           history=session.get('food_history', []),
                           food_list=list(FOOD_DATA.keys()))  # for dropdown


@app.route('/add-food', methods=['POST'])
def add_food():
    food_item = request.json.get('food')
    calories = FOOD_DATA.get(food_item.lower(), 0)

    # Initialize food history if not present
    if 'food_history' not in session:
        session['food_history'] = []

    session['food_history'].append({'item': food_item, 'calories': calories})
    session['intake'] += calories
    session.modified = True  # force update

    return jsonify({
        'calories': calories,
        'total_intake': session['intake'],
        'remaining': max(session['required'] - session['intake'], 0),
        'history': session['food_history']
    })


@app.route('/add-burn', methods=['POST'])
def add_burn():
    burned = request.json.get('burn')
    session['burned'] += int(burned)
    return jsonify({'total_burned': session['burned']})


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


@app.route('/export-report', methods=['GET'])
def export_report():
    report = {
        'name': session.get('name'),
        'required_calories': session.get('required'),
        'calories_intake': session.get('intake'),
        'calories_burned': session.get('burned'),
        'remaining': max(session.get('required', 0) - session.get('intake', 0), 0),
        'food_history': session.get('food_history', [])
    }

    buffer = io.BytesIO()
    buffer.write(json.dumps(report, indent=4).encode('utf-8'))
    buffer.seek(0)

    return send_file(buffer, mimetype='application/json',
                     as_attachment=True, download_name='calorie_report.json')
