#!/usr/bin/python3
"""This module contains methods to start your API."""

from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext()
def handle_teardown(exception):
    return storage.close()


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
