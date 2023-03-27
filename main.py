import os

from dotenv import load_dotenv
from flask import Flask
from db import db


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from auth import auth
    app.register_blueprint(auth)
    from home import home
    app.register_blueprint(home)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', debug=True)
