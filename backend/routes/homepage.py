from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__)

@homepage.route('/home')
def home():
    return render_template('homepage.html')

