#!/usr/bin/python3
""" View for State objects for the API """
#from flask import Flask, jsonify, request, abort, make_response
#from api.v1.views import app_views
#from models import storage
#from models.state import State
#
#
#@app_views.route('/states', methods=['GET'], strict_slashes=False)
#def get_states():
#    """Retrieves a list of all state objects"""
#    states = []
#    for state in storage.all(State).values():
#        states.append(state.to_dict())
#    return jsonify(states)
#
#
#@app_views.route('/states/<string:state_id>',
#                 methods=['GET'], strict_slashes=False)
#def get_state(state_id):
#    """Retrieves a State object by ID"""
#    state = storage.get(State, state_id)
#    if state is None:
#        abort(404)
#    return jsonify(state.to_dict())
#
#
#@app_views.route(
#    '/states/<string:state_id>', methods=['DELETE'],
#    strict_slashes=False
#)
#def delete_state(state_id):
#    """Deletes a State object by ID"""
#    state = storage.get(State, state_id)
#    if state is None:
#        abort(404)
#    state.delete()
#    storage.save()
#    return (jsonify({}))
#
#
#@app_views.route('/states', methods=['POST'], strict_slashes=False)
#def create_state():
#    """Creates a new State with the status code 201"""
#    if not request.get_json():
#        return make_response(jsonify({'error': 'Not a JSON'}), 400)
#    if 'name' not in request.get_json():
#        return make_response(jsonify({'error': 'Missing name'}), 400)
#    state = State(**request.get_json())
#    state.save()
#    return make_response(jsonify(state.to_dict()), 201)
#
#
#@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
#def update_state(state_id):
#    """Updates a state object by ID"""
#    state = storage.get(State, state_id)
#    print(state)
#    if state is None:
#        abort(404)
#    if not request.get_json():
#        return make_response(jsonify({'error': 'Not a JSON'}), 400)
#    for attr, val in request.get_json().items():
#        if attr not in ['id', 'created_at', 'updated_at']:
#            setattr(state, attr, val)
#    state.save()
#    return jsonify(state.to_dict())
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state():
    """Retrieves the list of all State objects"""
    objs = storage.all(State)
    return jsonify([obj.to_dict() for obj in objs.values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def single_state(state_id):
    """Retrieves a State object"""
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_state(state_id):
    """Deletes a State object"""
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    obj.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """Returns the new State with the status code 201"""
    new_obj = request.get_json()
    if not new_obj:
        abort(400, "Not a JSON")
    if 'name' not in new_obj:
        abort(400, "Missing name")
    obj = State(**new_obj)
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """ Updates a State object """
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    for k, v in req.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(obj, k, v)

    storage.save()
    return make_response(jsonify(obj.to_dict()), 200)
