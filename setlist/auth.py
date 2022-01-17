from sqlite3 import IntegrityError
from flask import Blueprint, render_template, url_for,redirect
from flask_login import login_required, login_user, current_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from setlist.models import Users
from .forms import CreateAccount, LoginForm

from . import db 

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_account = Users.query.filter_by(email=email).first()

        print(user_account.email, user_account.password)

        if user_account and check_password_hash(
            pwhash=user_account.password, password=password):
            login_user(user_account)
            return redirect(url_for('setview.home'))
        else:
            print('Wrong pw / email')
            return redirect('login')


    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    # logs out current user
    logout_user()
    return redirect(url_for('setview.home'))


@auth.route('/join', methods=['GET', 'POST'])
def signup():
    # allows users to sign up for setlist
    form = CreateAccount()

    if form.validate_on_submit():
        # load data from form and hash + salt password
        name = form.name.data
        email = form.email.data.lower()

        if form.password.data == form.password2.data:
            password = generate_password_hash(
                form.password.data,
                method='pbkdf2:sha256',
                salt_length=8)
            try: 
                new_user = Users(
                    name=name,
                    email=email,
                    password=password
                )
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect(url_for('setview.home'))
            except Exception as E:
                print('Email Taken')
                return redirect(url_for('setview.home'))
        else:
            print('Passwords Do Not Match')





    return render_template('auth/signup.html', form=form)