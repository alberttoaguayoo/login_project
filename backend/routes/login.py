from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.db import get_db_connection

login= Blueprint('login', __name__)

@login.route('/', methods=['GET', 'POST'])
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
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user and user[3] == password:
            return redirect(url_for('homepage.home'))
        else:
            flash('Credenciales incorrectas')
    return render_template('login.html')

