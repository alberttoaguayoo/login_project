from flask import Blueprint, render_template, session
from backend.utils.auth import login_required

homepage = Blueprint('homepage', __name__)

@homepage.route('/home')
@login_required
def home():
    return render_template('homepage.html', user=session.get('user'))

