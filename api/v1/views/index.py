#!/usr/bin/python3
"""index.py module page"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns API Json satus"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def getstats():
    """retrieves the number of each objects by type"""
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objt = {}
    for i in range(len(classes)):
        num_objt[names[i]] = storage.count(classes[i])

    return jsonify(num_objt)
