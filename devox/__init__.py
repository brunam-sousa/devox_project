from flask import Flask


# function "create_app" is a Application Factory
# create a function named create_app that initializes the app and returns it
def create_app():
    # define a instance folder ( a folder outside that hold local data)
    app = Flask(__name__)
    #app = Flask(__name__, instance_relative_config=True, instance_path='/home/bruna/devox_conf')
    app.config['SECRET_KEY'] = 'dev'

    
    # importing modules
    from devox import pages    
    from .authentication import auth
    from .authentication.auth import login_m
    from .authentication.users import User

    login_m.init_app(app)

    @login_m.user_loader
    def load_user(user_id):
        user = User()
        return user    
        
    """ Blueprint registrations """
    # connect the "pages" blueprint with the flask project
    app.register_blueprint(pages.bp_pages)
    #registering blueprint
    app.register_blueprint(auth.bp_auth)
    """ end of Blueprint registrations """

    return app