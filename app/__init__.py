from flask import Flask
import os

app = Flask(__name__)
app.secret_key = 'nexus_secret_key_pro'
# Database file will be created in the instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False