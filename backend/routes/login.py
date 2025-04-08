from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from backend.db import get_db_connection
from werkzeug.security import check_password_hash

login= Blueprint('login', __name__)

index = Blueprint('index', __name__)
@index.route('/', methods=['GET', 'POST'])
def index_view():
    return render_template('index.html')

@login.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
        SELECT u.id, u.username, u.email, a.password
        FROM users u
        JOIN auth a ON u.id = a.user_id
        WHERE u.username = %s
        """, (user,))
        user_data = cur.fetchone()
        cur.close()
        conn.close()
        
        if user_data and check_password_hash(user_data[3], password):
            session['user_id'] = user_data[0]
            session['username'] = user_data[1]
            return redirect(url_for('homepage.home'))
        else:
            flash('Credenciales incorrectas')
    return render_template('login.html')

