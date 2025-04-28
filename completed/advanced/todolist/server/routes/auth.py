from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from ..models import db, User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and Password expected'}), 400

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 400

    login_user(user)
    return jsonify({
        'message': 'Login successful',
        'user': {
            'id': user.user_id,
            'username': user.username,
            'email': user.email
        }
    })


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    if not all([username, email, password]):
        return jsonify({'error': 'Missing fields: username, passsword, and/or email'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username taken'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email taken'}), 400

    new_user = User(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    new_user.set_password(password)
    db.session.add(new_user)

    db.session.commit()
    return jsonify({
        'message': 'Registration successful',
        'user': {
            'id': new_user.user_id,
            'username': new_user.username,
            'email': new_user.email,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name
        }
    }), 201
