import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from db import user_db


basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'auth.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from auth import auth
    app.register_blueprint(auth)
    from home import home
    app.register_blueprint(home)

    user_db.init_app(app)
    with app.app_context():
        user_db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0')
