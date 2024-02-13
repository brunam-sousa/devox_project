from flask import Flask
from devox import pages


# function "create_app" is a Application Factory
# create a function named create_app that initializes the app and returns it
def create_app():
    # define a instance folder ( a folder outside that hold local data)
    app = Flask(__name__)
    #app = Flask(__name__, instance_relative_config=True, instance_path='/home/bruna/devox_conf')
    app.config['SECRET_KEY'] = 'dev'
    
    """Blueprint registrations"""
    # connect the "pages" blueprint with the flask project
    app.register_blueprint(pages.bp)
    
    # import of authentication module
    from .authentication import auth
    #registering blueprint
    app.register_blueprint(auth.bp)

    return app