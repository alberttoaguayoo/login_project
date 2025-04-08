import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
    DB_USER = os.getenv('DB_USER', 'admin')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password_segura')
    DB_NAME = os.getenv('DB_NAME', 'login_db')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
