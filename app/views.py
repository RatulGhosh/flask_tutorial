from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	#return "Hello, World!"
    user = {'nickname': 'Ratul'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
