from flask import Blueprint, render_template
from flask_login import login_required

# blueprint are modules that contain related views

# create the instance of Blueprint. "pages" is the name of blueprint
bp_pages = Blueprint("pages", __name__)


@bp_pages.route("/")
def home():
    # By default, Flask expects your templates to be in a templates/ directory
    return render_template("pages/home.html")


@bp_pages.route("/about")
def about():
    return render_template("pages/about.html")

@bp_pages.route('/profile')
@login_required
def profile():
    return render_template("pages/home.html")
