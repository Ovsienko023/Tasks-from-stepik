from flask import render_template, flash, redirect, url_for
from flask import request, session
from app import app
from app.forms import LoginForm
from flask_login import logout_user

from flask_login import current_user, login_user
from app.models import User
from flask_login import login_required

@app.route('/')
@app.route('/index')
@login_required
def index():
    # print(current_user.is_authenticated)
    # print(current_user.__dir__())
    if current_user.is_authenticated:
        print('зашел')
    # print(session)
    return {"Status": True}


@app.route('/login', methods = ['GET', 'POST'])
def login():

    # print('!!!!!!!!!!!!!!!!',current_user)
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        # print('зашел')
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        user = User(form.username.data, form.password.data)
        login_user(user, remember=form.remember_me.data)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))