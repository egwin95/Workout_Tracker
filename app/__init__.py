from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
# login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

    db.init_app(app)
   # login_manager.init_app(app)
   # login_manager.login_view = 'login'  # optional: redirect unauthorized users

   # from .models import User  # <-- Add this
   # @login_manager.user_loader
   # def load_user(user_id):
     #   return User.query.get(int(user_id))

    from .routes import main
    app.register_blueprint(main)

    return app

