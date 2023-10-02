#!/usr/bin/python3
"""index.py page"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns API Json satus"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """Retrieve the number of objects by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)


if __name__ == "__main__":
    pass
