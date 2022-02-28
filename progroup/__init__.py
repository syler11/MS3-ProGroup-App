import os
from flask import (Flask)
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env

# App variables for setup and mongodb connectivity
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
mongo.init_app(app)


def create_app():
    """
    Create an app with the authentication, errors, profiles, reservations,
    users blueprint routes
    """
    # Import the routes
    from progroup.authentication.routes import authentication
    from progroup.errors.routes import errors
    from progroup.profiles.routes import profiles
    from progroup.reservations.routes import reservations
    from progroup.users.routes import users
    # Register the routes with the app
    app.register_blueprint(authentication)
    app.register_blueprint(errors)
    app.register_blueprint(profiles)
    app.register_blueprint(reservations)
    app.register_blueprint(users)
    # Return the app
    return app
