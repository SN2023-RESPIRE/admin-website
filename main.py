from flask import Flask, render_template

from auth import auth

app = Flask(__name__)
app.register_blueprint(auth)


@app.route('/')
def home():
    return render_template('pages/index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
