import os
from flask import url_for, redirect, render_template, flash, g, session
from app import app, APP_STATIC
from app.models import *

@app.route('/')
def index():
	filepath = os.path.join(APP_STATIC, 'iris.csv')
	df = pd.read_csv(filepath)
	return render_template('index.html', headers=df.columns, data=probability(df))