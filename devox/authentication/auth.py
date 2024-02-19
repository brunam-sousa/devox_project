from flask import (
    Blueprint, redirect, render_template, request, url_for, flash)
from flask_login import login_user, LoginManager
from .users import User


bp_auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

login_m = LoginManager()

@bp_auth.route('/index', methods=('GET', 'POST'))
def index():
    if request.method != 'POST':
        return render_template('form_login.html')
    else: return login()

@bp_auth.route('/login')
def login():
    error = None
    username = request.form.get('username')
    password = request.form.get('password')

    if  username == 'bruna' and  password == 'teste':
        user = User()
        login_user(user)
        return redirect(url_for('pages.profile'))
    else:
        error = 'Dados de usuario e/ou senha incorreto(s)'
        flash(error)
        return render_template('form_login.html', error=error )