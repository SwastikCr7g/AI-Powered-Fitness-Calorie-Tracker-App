from flask import Flask
import os
import json  # 👈 Jaruri import JSON parsing ke liye

app = Flask(__name__)
app.secret_key = 'nexus_secret_key_pro'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🛠️ CUSTOM JINJA2 FILTER (Fixes: No filter named 'from_json')
# Ye function string ko wapas Python dictionary/list mein convert karega
@app.template_filter('from_json')
def from_json_filter(value):
    try:
        return json.loads(value) if value else {}
    except (ValueError, TypeError):
        return {}

# Yahan aapke baaki imports aayenge (models, routes etc.)
# from app import routes, models