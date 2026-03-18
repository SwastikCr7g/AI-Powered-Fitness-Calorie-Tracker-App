from app import app
# IMPORTANT: Routes ko yahan import karna zaroori hai taaki Flask unhe pehchan sake
from app import routes
import json

@app.template_filter('from_json')
def from_json_filter(value):
    try:
        return json.loads(value)
    except:
        return []

if __name__ == '__main__':
    app.run(debug=True)