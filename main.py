from flask import Flask, render_template

from auth import auth
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.register_blueprint(auth)


@app.route('/')
def home():
    return render_template('pages/index.html')


if __name__ == '__main__':
    db.init_app(app)
    app.run('0.0.0.0', debug=True)
