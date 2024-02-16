from flask import (
    Blueprint, redirect, render_template, request, session, url_for, flash)

from .users import User

#flask-login provides user session management
#from flask_login import LoginManager


bp_auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')
#bp = Blueprint('auth', __name__, url_prefix='/teste')

#login_m = LoginManager()
#login_m.init_app(app)
# used to reload the user object from the user ID stored in the session
# return 'None' if ID is not valid
#@login_m.user_loader
#def load_user(user_id):
#    return User.get(user_id)

@bp_auth.route('/index', methods=('GET', 'POST'))
def index():
    if request.method != 'POST':
        return render_template('form_login.html')
    else: return login()

@bp_auth.route('/login')
def login():
    error = None

    if request.form.get('username') == User.username and request.form.get('password') == User.password:
        flash('You were successfully logged in')
        return redirect(url_for('pages.home'))
    else:
        error = 'Dados de usuario e/ou senha incorreto(s)'
        flash(error)
        return render_template('form_login.html', error=error )