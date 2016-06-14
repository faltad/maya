from flask import Flask, render_template

import sqlalchemy
import sys

from core_utils.config import Config

sql_url = Config.get_sqlalchemy_url()
engine = sqlalchemy.create_engine(sql_url, echo=True)
try:
    conn = engine.connect()
except sqlalchemy.exc.OperationalError as e:
    print(str(e))
    sys.exit(-1)


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return "hello"
