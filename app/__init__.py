from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ.get("SECRET_KEY", "fallback_secret")

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, "fitness.db")

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{db_path}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # ✅ Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app