from flask import Blueprint, render_template
from flask_login import login_required

# blueprint are modules that contain related views

# create the instance of Blueprint. "pages" is the name of blueprint
bp_profile = Blueprint("profile", __name__, url_prefix='/user')


@bp_profile.route("/home")
@login_required
def home():
    return render_template("user_pages/profile.html")

@bp_profile.route("/dashboard")
@login_required
def dashboard():
    return render_template("user_pages/profile.html")

@bp_profile.route("/search_product")
@login_required
def search_product():
    return render_template("user_pages/profile.html")

@bp_profile.route("/profile")
@login_required
def profile():
    return render_template("user_pages/profile.html")