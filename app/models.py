from flask_sqlalchemy import SQLAlchemy
from app import app

# Database instance initialize
db = SQLAlchemy(app)

class User(db.Model):
    """
    Fitness Pro - Master User Model
    Stores persistent bio-data and daily nutritional tracking.
    """
    __tablename__ = 'users'

    # Primary Identification
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Bio-Data (Stored for BMI & Re-calculation)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    required = db.Column(db.Integer, nullable=False)  # Daily Calorie Goal (TDEE)

    # Daily Tracking Metrics (Defaults to 0.0)
    intake = db.Column(db.Float, default=0.0)
    burned = db.Column(db.Float, default=0.0)

    # Macro-Nutrients tracking (Grams)
    protein = db.Column(db.Float, default=0.0)
    carbs = db.Column(db.Float, default=0.0)
    fats = db.Column(db.Float, default=0.0)

    # Hydration tracking (Glasses of water)
    water = db.Column(db.Integer, default=0)

    # System Logs (Stored as a stringified JSON list)
    # Important: Default is '[]' string to prevent Jinja2 filter crashes
    history = db.Column(db.Text, default='[]')

    def __repr__(self):
        return f'<User {self.name} - Target: {self.required}kcal>'