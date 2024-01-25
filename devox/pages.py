from flask import Blueprint, render_template

#blueprint are modules that contain related views

#create the instance of Blueprint. "pages" is the name of blueprint
bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    #By default, Flask expects your templates to be in a templates/ directory
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")