from . import db 
from flask_login import UserMixin
from sqlalchemy.orm import relationship


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250),)
    email = db.Column(db.String(300), nullable=False, unique=True)

    # Link Set list Database to User
    set_list = relationship('UserSetList', back_populates='set_owner')


class UserSetList(db.Model):
    __tablename__ = 'usersetlist'

    id = db.Column(db.Integer, primary_key=True)
    set_name = db.Column(db.String(200))
    description = db.Column(db.String(500))
    # song_id = db.Column(db.Integer, db.ForeignKey('songs.id')) # change to setlist songs
    songs = relationship('UserSetListSongs')

    group_members = relationship("GroupMembers") # , back_populates="setlist")
    set_owner = relationship('Users', back_populates="set_list")
    set_owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class GroupMembers(db.Model):
    __tablename__ = 'groupmembers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(300), nullable=False)
    role = db.Column(db.String(100),)

    # Setup two way relationship between group members and setlist
    setlist_id = db.Column(db.Integer, db.ForeignKey('usersetlist.id'))
    # setlist = relationship("UserSetList", back_populates="group_members")


class Songs(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(150), nullable=False)
    song_url = db.Column(db.String(150), unique=True)


class UserSetListSongs(db.Model):
    __tablename__ = 'usersetlistsongs'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    setlist_id = db.Column(db.Integer, db.ForeignKey('usersetlist.id'))
    song_key = db.Column(db.String(5))
    song_bpm = db.Column(db.Float)
    song_notes = db.Column(db.String(500))