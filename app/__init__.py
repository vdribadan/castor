from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    # Initialize Flask app
    app = Flask(__name__)

    # Configure the app for testing or production
    if config_name == 'testing':
        # Use in-memory SQLite database for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
    else:
        # Use file-based SQLite database for production
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fruits.db'

    db.init_app(app)

    # Import and register the Blueprint for API routes
    from app.routes import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
