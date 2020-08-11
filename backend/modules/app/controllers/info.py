''' controller and routes for users '''
import os
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity)
from app import app, mongo, flask_bcrypt, jwt
from app.schemas import validate_user
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/feed', methods=['GET'])
@jwt_required
def feed():
    if request.method == 'GET':
        data = {"message": "Cat Fed!"}
        return jsonify({'ok': True, 'data': data}), 200

@app.route('/user', methods=['GET', 'DELETE', 'PATCH'])
@jwt_required
def user():
    ''' route read user '''
    if request.method == 'GET':
        query = request.args
        data = mongo.db.users.find_one(query, {"_id": 0})
        return jsonify({'ok': True, 'data': data}), 200

    data = request.get_json()
    if request.method == 'DELETE':
        if data.get('email', None) is not None:
            db_response = mongo.db.users.delete_one({'email': data['email']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH':
        if data.get('query', {}) != {}:
            mongo.db.users.update_one(
                data['query'], {'$set': data.get('payload', {})})
            return jsonify({'ok': True, 'message': 'record updated'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
