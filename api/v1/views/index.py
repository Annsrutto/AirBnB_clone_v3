#!/usr/bin/python3
"""create a route /status on the object app_views that returns a JSON"""

from api.v1.views import app_views
from flask import Jsonify


@app_views.route('/status', methods=[GET])
def index():
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', methods=[GET])
def retrieve_stats():
    classes_count = {}
    for cls in storage.classes.values():
        classes_count[cls.__name__] = storage.count(cls)
    return jsonify(classes_count)
