from flask import (
    Blueprint, redirect, render_template, request, session, url_for, flash)

bp = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')
#bp = Blueprint('auth', __name__, url_prefix='/teste')

#array with ficticional users params (to tests)
testUsers = [1, 'bruna', 'senhateste']

#function used to compare username and password and create a user session 
@bp.route('/index', methods=('GET', 'POST'))
def index():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == testUsers[1] and password == testUsers[2]:
            session.clear()
            session['user_id'] = testUsers[0] 
            flash('You were successfully logged in')
            return redirect(url_for('pages.home'))
        else:
            error = 'Dados de usuario e/ou senha incorreto(s)'
            flash(error)
            return render_template('form_login.html', error=error )
        
    return render_template('form_login.html')