from flask import Flask
import os

app = Flask(__name__)

# ✅ Secure Secret Key
app.secret_key = os.environ.get("SECRET_KEY", "fallback_secret")

# ✅ Database Config (Render Safe)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "fitness.db")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL",
    f"sqlite:///{db_path}"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False