from flask import Flask, request, jsonify

import datetime
import os
import subprocess
import logging

from models.client import Client
from models.request import Request
from database import db_session

from core_utils.build import verify_hash


# Start the flask app
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/deploy')
def deploy():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    signature = request.headers.get('X-Hub-Signature')
    data = request.data
    if verify_hash(data, signature):
        if request.headers.get('X-GitHub-Event') == 'push':
            payload = request.get_json()
            if payload['commits'][0]['distinct']:
                try:
                    cmd_output = subprocess.call(['python3', base_dir + '/core_utils/build.py'])
                    logging.info('Deploy OK')
                    return jsonify({'msg': str(cmd_output)})
                except Exception as error:
                    logging.error(str(error))
                    return jsonify({'msg': str(error)})


@app.route('/', defaults={'path': ''}, methods=["GET", "POST", "DELETE", "PUT"])
@app.route('/<path:path>', methods=["GET", "POST", "DELETE", "PUT"])
def catch_all(path):
    path = "/" + path
    c = db_session.query(Client).filter(Client.ip == request.remote_addr).first()
    if c is None:
        c = Client(ip=request.remote_addr)
        db_session.add(c)

    r = Request(route=path, time=datetime.datetime.now(), post_data=request.get_data(), headers=request.headers, client=c, method=request.method)
    db_session.add(r)
    db_session.commit()
    return "", 200
