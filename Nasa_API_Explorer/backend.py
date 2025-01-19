from flask import request, jsonify
from . import app
from .models import User
from . import db
from flask_login import login_user, current_user, logout_user, login_required
from .Nasa_EONET import *

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        try:
            data = request.json
            if not data or 'username' not in data:
                return jsonify({'error': 'Username is required'}), 400 # Bad request

            elif data['username'] == User.query.filter_by(email=data['username']).first():
                return jsonify({'error': 'Username already exists'}), 400 # Bad request

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
            data = request.json # Get the JSON data from the request
            if not data or 'username' not in data:
                return jsonify({'error': 'Username is required'}), 400  # Bad request

            username = data['username']
            password = data['password']
            user = User.query.filter_by(email=username).first() # Query the database for the user
            if user and user.password == password:  # Check if the user exists and the password is correct
                login_user(user)
                return jsonify({'message': f"{username} successfully logged in"}), 200 # OK
            else:
                return jsonify({'error': 'Invalid username or password'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 500 # Internal server error

    elif request.method == 'GET':
        return jsonify({'message': 'Welcome to the login page. Please send a POST request to log in.'})

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Successfully logged out'}), 200

@app.route('/natural_hazards_events', methods=['GET'])
def natural_hazards_events():
    events = get_natural_disasters_by_events()
    return jsonify({'events': events}), 200

@app.route('/natural_hazards_categories', methods=['GET'])
def natural_hazards_categories():
    category = get_natural_disasters_by_categories()
    return jsonify({'categories': category}), 200
