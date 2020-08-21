''' controller and routes for users '''
import os
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity)
from app import app, mongo, flask_bcrypt, jwt
from app.schemas import validate_user
import logger
import RPi.GPIO as GPIO
import time

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))



def triggerMachine():
    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
    p.start(2.5)  # Initialization

    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)



@app.route('/feed', methods=['GET'])
@jwt_required
def feed():
    if request.method == 'GET':
        triggerMachine()

        current_user = get_jwt_identity()

        t = time.localtime()
        current_time = time.strftime("%d %b %Y %Hh%M", t)

        food = {'type': "Croquettes", 'date': current_time, 'feeder': current_user["email"]}

        mongo.db.food.insert_one(food)

        return jsonify({'ok': True, 'data': food}), 200
    if request.method == 'DELETE':
        mongo.db.drop_collection('food')
        return jsonify({'ok': True}), 200

@app.route('/info', methods=['GET'])
#@jwt_required
def info():
    ''' route read user '''
    if request.method == 'GET':

        data = mongo.db.food.find({})
        docs = list(data)

        return jsonify({'ok': True, 'data': docs}), 200




