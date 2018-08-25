import os
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.debug = True

bs = Bootstrap(app) #flask-bootstrap

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

from app import views, models
