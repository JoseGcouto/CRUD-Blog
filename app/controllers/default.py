from app import app, db, lm
from flask import render_template, flash ,redirect, url_for
from app.models.tables import User
from app.models.forms import LoginForm
from flask_login import login_user, logout_user


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/index/<user>')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.Password == form.password.data:
            login_user(user)
            flash('Logged in.')
        else:
            flash('Invalid Login')
    return render_template('login.html', form=form )


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))