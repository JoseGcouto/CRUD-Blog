from app import app, db
from flask import render_template
from app.models.tables import User
from app.models.forms import LoginForm



@app.route('/index/<user>')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    print(form.username.data)
    print(form.password.data)
    return render_template('login.html', form=form )