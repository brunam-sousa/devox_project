from .db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

from flask import (
    Blueprint, redirect, render_template, request, url_for, flash)

#from flask_login import login_user, logout_user, login_required
#'LoginManager' object is used to hold the settings used for logging in. 
#Instances of LoginManager are not bound to specific apps
#will be registred on the factory function 'create_app'.
from flask_login import LoginManager

from devox.db import get_db
#from .users import User


login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

#create a blueprint named 'auth'
#'url_prefix' will be prepended to all the URLs associated with the blueprint.
bp_auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

@bp_auth.route('/index', methods=('GET', 'POST'))
def index():
    if request.method != 'POST':
        return render_template('auth/form_login.html')
    else: return login()

# processing de form for user register
@bp_auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username,password) VALUES (?,?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registred"
            else:
                return redirect(url_for("auth.login"))

#if URL = auth/login
@bp_auth.route('/login')
def login():
    error = None
    username = request.form.get('username')
    password = request.form.get('password')
    db = get_db()
    user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

    if user is None or user['password'] != password :
        error = 'Incorrect username or password'
    
    if error is None:
        user = User()
        login_user(user)
        return redirect(url_for('profile.home'))
 
    flash(error)
    
    return render_template('auth/form_login.html', error=error )

#@bp_auth.route("/logout")
#@login_required
#def logout():
#    logout_user()
#    return render_template("pages/home.html")