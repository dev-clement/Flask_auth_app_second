from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'LOGIN'

@auth.route('/register')
def register():
    return 'REGISTER'

@auth.route('/logout')
def logout():
    return 'LOGOUT'