from app import app
import app.routes   # ✅ VERY IMPORTANT (routes register karega)

# For Gunicorn
application = app

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)