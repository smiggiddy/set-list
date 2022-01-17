from ast import Pass
from tokenize import String
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField
from wtforms.fields.simple import EmailField, PasswordField, HiddenField
from wtforms.validators import DataRequired, URL, Email


class CreateAccount(FlaskForm):
    # Used to Create An Account form
    name = StringField("First Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddGroupMembers(FlaskForm):
    # Form to Add Who Needs Access to Set List
    set_list_name = HiddenField()
    name = StringField('Member Name', validators=[DataRequired()])
    email = EmailField("Member's Email", validators=[DataRequired()])
    role = StringField("Member's Role", validators=[DataRequired()])
    submit = SubmitField("Submit")


class CreateSetList(FlaskForm):
    # Create A New Setlist
    set_name = StringField("Set List Name", validators=[DataRequired()])
    description = StringField("Set Description", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddSongs(FlaskForm):
    # For Adding Songs to Set List
    song = StringField("Add Song", validators=[DataRequired()])
    key = StringField("Key Signature")
    bpm = StringField("Bpm")
    notes = StringField("Song notes")
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    # allows user to log on
    email = StringField("Email Address")
    password = PasswordField("Password")
    submit = SubmitField('Submit')
