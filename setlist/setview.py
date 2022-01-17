from flask import Blueprint, url_for, render_template

# from setlist.auth import * # TODO correct this import
from flask_login import login_required, current_user
from .forms import CreateSetList

from .models import UserSetList

from . import db

setview = Blueprint('setview', __name__)

@setview.route('/', methods=['GET', 'POST'])
def home():
    # main home page
    return render_template("dashboard.html")


@setview.route('/new', methods=['GET', 'POST'])
@login_required
def add():
    # Method to view and add setlists
    form = CreateSetList()

    if form.validate_on_submit():
        set_name = form.set_name.data
        # description = form.description.data
        user_id = current_user.get_id()

        new_set = UserSetList(
            set_name= set_name,
            set_owner= current_user,
        )
        db.session.add(new_set)
        db.session.commit()

    return render_template('set/add.html', form=form)


@setview.route('/modify', methods=['GET', 'POST'])
@login_required
def modify_set():
    # used to add group members / delete setlist etc
    return 'modify'





