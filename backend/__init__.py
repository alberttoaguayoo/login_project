from flask import Flask
from .config import Config 
from .routes.login import login
from .routes.homepage import homepage

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(login)
    app.register_blueprint(homepage)


    return app

