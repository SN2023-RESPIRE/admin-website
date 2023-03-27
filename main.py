from flask import Flask
import routes

app = Flask(__name__)
app.register_blueprint(routes.bp)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
