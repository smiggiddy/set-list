from flask import Blueprint, url_for, render_template

# from setlist.auth import * # TODO correct this import
from flask_login import login_required, current_user

setview = Blueprint('setview', __name__)

@setview.route('/', methods=['GET', 'POST'])
def home():
    # main home page
    return "It's working"


@setview.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Method to view and add setlists
    return 'Dashboard'


@setview.route('/modify', methods=['GET', 'POST'])
# @login_required
def modify_set():
    # used to add group members / delete setlist etc
    return 'modify'





