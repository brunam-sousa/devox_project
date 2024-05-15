import os
# file '__init__' will tells Python that the 'devox' directory should be treated as a package
from flask import Flask

# using Application Factory
# create a function named create_app that initializes and configure the app and returns it
def create_app():

    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'dev'
    app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'devox.sqlite')
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # importing modules and initializing
    from . import db
    db.init_app(app) # command to initialize the DB: $ flask --app flaskr init-db

    from . import bpauth
    # configuring the LoginManager object
    bpauth.login_manager.init_app(app)


    # import blueprints
    #from . import bpauth
    from . import pages    
    
    """ Blueprint registrations """
    # connect the blueprint with the flask project
    app.register_blueprint(pages.bp_pages)
    app.register_blueprint(bpauth.bp_auth)
    """ end of Blueprint registrations """

    #@login_m.user_loader
    #def load_user(user_id):
    #    user = User()
    #    return user    

    return app