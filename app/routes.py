from flask import render_template, request, redirect, session, jsonify, send_file
from app import app
from app.models import db, User
from app.utils.calorie_predictor import calculate_required_calories, get_bmi_status
from app.utils.food_database import FOOD_DATA, indian_foods
import io
import json

# Database initialize on startup
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def login():
    """System Authentication & Bio-Data Initialization"""
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        h, w = float(request.form['height']), float(request.form['weight'])
        act = request.form['activity_level']

        # Calculate daily fuel requirement
        req = calculate_required_calories(gender, age, w, h, act)

        # Persistence Check: Update existing user or create new
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name, required=req, weight=w, height=h)
            db.session.add(user)
        else:
            user.required = req
            user.weight, user.height = w, h

        db.session.commit()
        session['user_id'] = user.id
        return redirect('/dashboard')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    """Central Command Center Dashboard"""
    u_id = session.get('user_id')
    if not u_id:
        return redirect('/')

    user = User.query.get(u_id)
    if not user:
        return redirect('/')

    # Calculate Bio-Metrics
    bmi, status, color = get_bmi_status(user.weight, user.height)

    # AI Suggestion Logic - Analyzing remaining capacity
    remaining = user.required - user.intake
    suggestion = "System Optimized. Continue following the protocol."
    if remaining > 150:
        # Filter healthy options from the database within the remaining limit
        opts = [f['name'] for f in indian_foods if 50 < f['calories'] <= remaining]
        if opts:
            suggestion = f"AI Recommends: Consume '{opts[0]}' to hit your energy target."

    return render_template('dashboard.html',
                           user=user,
                           bmi=bmi,
                           status=status,
                           s_color=color,
                           suggestion=suggestion,
                           food_list=sorted([f['name'] for f in FOOD_DATA.values()]))


@app.route('/add-food', methods=['POST'])
def add_food():
    """Log Nutritional Intake into System"""
    user = User.query.get(session.get('user_id'))
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    food_name = request.json.get('food').lower()
    f = FOOD_DATA.get(food_name)

    if f:
        # Update Core Stats
        user.intake += f['calories']
        user.protein += f.get('protein', 0)
        user.carbs += f.get('carbs', 0)
        user.fats += f.get('fats', 0)

        # Update History JSON
        try:
            hist = json.loads(user.history)
        except:
            hist = []

        hist.insert(0, {'item': f['name'], 'calories': f['calories']})
        user.history = json.dumps(hist)

        db.session.commit()

        return jsonify({
            'total_intake': user.intake,
            'protein': round(user.protein, 1),
            'carbs': round(user.carbs, 1),
            'fats': round(user.fats, 1),
            'remaining': max(user.required - user.intake, 0),
            'history': hist,
            'calories': f['calories']
        })

    return jsonify({'error': 'Fuel source not identified'}), 404


@app.route('/add-water', methods=['POST'])
def add_water():
    """Log Hydration Level"""
    user = User.query.get(session.get('user_id'))
    if user:
        user.water += 1
        db.session.commit()
        return jsonify({'water': user.water})
    return jsonify({'error': 'Unauthorized'}), 401


@app.route('/add-burn', methods=['POST'])
def add_burn():
    """Log Energy Expulsion (Workouts)"""
    user = User.query.get(session.get('user_id'))
    if user:
        burned = request.json.get('burn', 0)
        try:
            user.burned += int(burned)
            db.session.commit()
            return jsonify({'total_burned': user.burned})
        except ValueError:
            return jsonify({'error': 'Invalid value'}), 400
    return jsonify({'error': 'Unauthorized'}), 401


@app.route('/logout', methods=['POST'])
def logout():
    """Clear Session & Go Offline"""
    session.clear()
    return redirect('/')


@app.route('/export-report', methods=['GET'])
def export_report():
    """Generate and Download Bio-Metrics Report"""
    user = User.query.get(session.get('user_id'))
    if not user:
        return redirect('/')

    bmi, status, _ = get_bmi_status(user.weight, user.height)

    report = {
        'user': user.name,
        'bio_metrics': {
            'BMI': bmi,
            'Status': status
        },
        'daily_stats': {
            'target_calories': user.required,
            'total_intake': user.intake,
            'total_burned': user.burned,
            'water_glasses': user.water,
            'macro_breakdown': {
                'protein_g': round(user.protein, 1),
                'carbs_g': round(user.carbs, 1),
                'fats_g': round(user.fats, 1)
            }
        },
        'food_logs': json.loads(user.history)
    }

    buffer = io.BytesIO()
    buffer.write(json.dumps(report, indent=4).encode('utf-8'))
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype='application/json',
        as_attachment=True,
        download_name=f'Nexus_{user.name}_Report.json'
    )