from flask import Flask
from devox import pages


# function "create_app" is a Application Factory
# create a function named create_app that initializes the app and returns it
def create_app():
    app = Flask(__name__)
    # connect the "pages" blueprint with the flask project
    app.register_blueprint(pages.bp)
    return app
