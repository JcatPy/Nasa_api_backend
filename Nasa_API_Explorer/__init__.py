from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
CORS(app, resources={r"/sign_up": {"origins": '*'}}, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database URI

db = SQLAlchemy(app)
login_manager = LoginManager(app) # login manager which handles all the sessions and cookies

from . import backend