from app import app
import app.routes

application = app   # ✅ THIS is BEST PRACTICE

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)