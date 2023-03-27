from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash

from models import User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('pages/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        flash('Username or password not given')
        return redirect(url_for('auth.login'))

    print(User.query.all())

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        flash('Invalid credentials given')
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('home.homepage'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
