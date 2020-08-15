''' controller and routes for users '''
import os
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity)
from app import app, mongo, flask_bcrypt, jwt
from app.schemas import validate_user
import logger
import time

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/feed', methods=['GET'])
@jwt_required
def feed():
    if request.method == 'GET':
        print("GET /feed")

        current_user = get_jwt_identity()

        print(current_user["email"])

        t = time.localtime()
        current_time = time.strftime("%d %b %Y %Hh%M", t)
        print(current_time)

        food = {'type': "Croquettes", 'date': current_time, 'feeder': current_user["email"]}
        mongo.db.food.insert_one(food)

        return jsonify({'ok': True, 'data': food}), 200
    if request.method == 'DELETE':
        mongo.db.drop_collection('food')
        return jsonify({'ok': True}), 200

@app.route('/info', methods=['GET', 'DELETE'])
#@jwt_required
def info():
    ''' route read user '''
    if request.method == 'GET':

        data = mongo.db.food.find({})
        docs = list(data)

        return jsonify({'ok': True, 'data': docs}), 200