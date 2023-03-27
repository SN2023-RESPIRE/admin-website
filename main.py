from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>HAI WORLD</h1><h6>kthxbye</h6>"


if __name__ == '__main__':
    app.run('0.0.0.0')
