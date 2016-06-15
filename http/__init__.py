from flask import Flask, render_template

import sqlalchemy
import sys

from core_utils.config import Config
from models.client import Client
from models.request import Request


# setup the sql connection/engine
sql_url = Config.get_sqlalchemy_url()
engine = sqlalchemy.create_engine(sql_url, echo=True)
try:
    conn = engine.connect()
except sqlalchemy.exc.OperationalError as e:
    print(str(e))
    sys.exit(-1)

# Start the flask app
app = Flask(__name__)

# Setup the models
Client.setup(engine, conn)
Request.setup(engine, conn)

@app.route('/', methods=["GET"])
def index():
    return "hello"
