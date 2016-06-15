from flask import Flask, request

import datetime

from models.client import Client
from models.request import Request
from database import db_session


# Start the flask app
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


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
