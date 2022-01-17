import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
DB_NAME = "setlist.db"

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'smig_proj'

    #import database configs 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize database to the app
    db.init_app(app)

    # import needed files
    from .setview import setview 
    from .auth import auth 

    # register the blueprints / views TODO
    app.register_blueprint(setview, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')


    # ensure the instance folder exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    #import the db models before creating the database
    from setlist.models import Users, UserSetList, GroupMembers, Songs

    create_db(app)

    # Initialize Bootstrap to App
    Bootstrap(app)


    # User Authentication Initialization
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))


    return app

def create_db(app):
    """Makes sure the database file exists"""

    if not os.path.exists('setlist/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')