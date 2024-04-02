#!/usr/bin/python3
"""create a route /status on the object app_views that returns a JSON"""

from api.v1.views import app_views
from flask import Jsonify

@app_views.route('/status', methods=[GET])
def index():
    return 'status' + ':' + ' ' + 'OK'
