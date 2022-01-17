from flask import Blueprint, url_for, render_template, redirect, request

# from setlist.auth import * # TODO correct this import
from flask_login import login_required, current_user
from .forms import CreateSetList, AddGroupMembers

from .models import UserSetList, GroupMembers

from . import db

setview = Blueprint('setview', __name__)

@setview.route('/', methods=['GET', 'POST'])
def home():
    # main home page
    user_sets = None
    if current_user.is_authenticated:
        user_sets = UserSetList.query.filter_by(set_owner=current_user).all()
        print(user_sets)
    if not user_sets:
        print('its empty')
        user_sets = None


    return render_template("dashboard.html", sets=user_sets)


@setview.route('/new', methods=['GET', 'POST'])
@login_required
def add():
    # Method to view and add setlists
    form = CreateSetList()

    if form.validate_on_submit():
        set_name = form.set_name.data
        description = form.description.data
        user_id = current_user.get_id()

        new_set = UserSetList(
            set_name= set_name,
            set_owner= current_user,
            description= description,
        )
        db.session.add(new_set)
        db.session.commit()
        return redirect(url_for('setview.add_members', setlist_id=new_set.id))

    return render_template('set/add.html', form=form)


@setview.route('/add-members', methods=['GET', 'POST'])
@login_required
def add_members():
    # used to add group members / delete setlist etc
    group = None
    set_id = request.args.get('setlist_id')
    form = AddGroupMembers()
    form.set_list_name = set_id


    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        role = form.role.data
        id = set_id

        group_member = GroupMembers(
            name = name,
            email = email,
            role = role, 
            setlist_id = id
        )

        db.session.add(group_member)
        db.session.commit()
        return redirect(url_for('setview.add_members', setlist_id=id))

    if set_id:
        group = GroupMembers.query.filter_by(setlist_id=set_id).all()

    return render_template('set/add_group.html', form=form, group = group)





