from flask import Blueprint, render_template, url_for
from flask_login import login_required, login_user, current_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from setlist.models import Users

from . import db 

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Allows users to login 
    return 'login'


@auth.route('/logout')
def logout():
    # logs out current user
    return 'logout'


@auth.route('/join', methods=['GET', 'POST'])
def signup():
    # allows users to sign up for setlist
    name = 'Test'
    password = 'Test'
    email = 'email@email.com'

    new_user = Users(name=name, password=password, email=email)
    db.session.add(new_user)
    db.session.commit()


    return 'registered'