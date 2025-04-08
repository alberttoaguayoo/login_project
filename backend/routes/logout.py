from flask import Blueprint, redirect, url_for, session, flash

logout = Blueprint('logout', __name__)

@logout.route('/logout')
def logout_view():
    session.pop('user_id', None)  # Eliminar 'user_id' de la sesion
    flash('Has cerrado sesión')
    return redirect(url_for('login.login_view'))
