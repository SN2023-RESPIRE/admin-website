import getpass

from db import user_db
from main import create_app
from models import User
from werkzeug.security import generate_password_hash

name = input('Enter full name (128 characters): ')
if len(name) <= 0 or len(name) >= 128:
    print('Please enter a valid name')
    exit(1)

username = input('Enter shortened username (32 characters): ')
if len(username) <= 0 or len(username) >= 32:
    print('Please enter a valid username')
    exit(1)

password = getpass.getpass('Enter password: ')
if len(password) <= 8:
    print('Please enter a password that has more than 8 characters')
    exit(1)

password2 = getpass.getpass('Confirm password: ')
if password != password2:
    print('Passwords do not match')
    exit(1)

user = User(name=name, username=username, password=generate_password_hash(password, method='sha256'))
app = create_app()
with app.app_context():
    user_db.session.add(user)
    user_db.session.commit()

print("User created successfully")
