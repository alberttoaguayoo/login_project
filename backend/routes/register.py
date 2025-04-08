from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from backend.db import get_db_connection
from time import sleep

register = Blueprint('register', __name__)

@register.route('/register', methods=['GET', 'POST'])
def register_view():
    if request.method == 'POST':
        #crear variables y almacenar lo que se agrega en el campo de registro del archivo html
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hash_pass = generate_password_hash(password, method='pbkdf2:sha256')
        #conectar con pg
        conn = get_db_connection()
        cur = conn.cursor()
        #insertar los datos
        try:
            cur.execute("""
            INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id
            """, (username, email))
            user_id = cur.fetchone()[0]

            cur.execute("""
            INSERT INTO auth (user_id, password) VALUES (%s, %s)
            """, (user_id, hash_pass))
            conn.commit()
            cur.close()
            conn.close()
            flash(f'usuario registrado, intenta iniciar sesion')
            return redirect(url_for('login.login_view'))
        except Exception as e:
            conn.rollback()
            cur.close()
            conn.close()
            flash(f'Error al registrar, intenta de nuevo: {str(e)}')
    return render_template('register.html')
	

