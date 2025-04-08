import os
from flask import Flask
from .config import Config 
from .routes.login import login, index
from .routes.homepage import homepage
from .routes.register import register
from .routes.logout import logout

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = os.environ.get('SECRET_KEY')
    app.register_blueprint(login)
    app.register_blueprint(homepage)
    app.register_blueprint(register)
    app.register_blueprint(logout)
    app.register_blueprint(index)


    return app

