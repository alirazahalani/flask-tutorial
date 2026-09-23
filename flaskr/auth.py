import functools
from sqlite3 import IntegrityError

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"

        if error is None:
            try:
                db.execute('Insert into user(username, password) values (?,?)',
                           (username, generate_password_hash(password)))
                db.commit()
            except db.IntegrityError:
                error = f"User (username) is already registerd."
            else:
                return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    import pdb; pdb.set_trace()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute('select * from user where username = ?', (username,)).fetchone()
        error = None

        if username is None:
            error = "Incorrect username"
        elif not check_password_hash(user['password'], password):
            error = "Incorrect password"

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect('index')

        flash(error)
    return render_template('auth/login.html')
    


    
    
    
