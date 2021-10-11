import os

# FLask
from flask import Flask

app_name = str(os.environ.get('FLASK_APP', __name__))
app = Flask(app_name)


@app.route('/')
def index():
    return 'Hello world from the Alpine Linux!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    debug = bool(os.environ.get('DEBUG', False))
    app.run(host='0.0.0.0', port=port, debug=debug)
