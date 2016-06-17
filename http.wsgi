import os, sys

def execfile(filename):
    globals = dict(__file__=filename)
    exec(open(filename).read(), globals)

activate_this = os.path.dirname(__file__) + '/venv/bin/activate_this.py'
execfile(activate_this)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http import app as application