from flask import request, jsonify
from . import app
from .models import User
from . import db


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        try:
            data = request.json
            if not data or 'username' not in data:
                return jsonify({'error': 'Username is required'}), 400 # Bad request

            username = data['username']
            password = data['password']
            user = User(email=username, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': f"Successfully signed up {username}"}), 200 # OK

        except Exception as e:
            return jsonify({'error': str(e)}), 500 # Internal server error

    # Handle GET request
    elif request.method == 'GET':
        # You can return a simple message or some default data for the GET request
        return jsonify({'message': 'Welcome to the sign-up page. Please send a POST request to sign up.'})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.json
            if not data or 'username' not in data:
                return jsonify({'error': 'Username is required'}), 400  # Bad request

        except Exception as e:
            return jsonify({'error': str(e)}), 500 # Internal server error

    elif request.method == 'GET':
        return jsonify({'message': 'Welcome to the login page. Please send a POST request to log in.'})
