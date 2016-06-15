from flask import Flask, render_template

import sys

from models.client import Client
from models.request import Request
from database import db_session


# Start the flask app
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=["GET"])
def index():
    buffer = Request(route="/")
    db_session.add(buffer)
    db_session.commit()
    return "hello"
