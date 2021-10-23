import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
mongo.init_app(app)

def init_app():
    """
    Initialize the app with blueprint routes
    """
    # Import blueprint routes
    from bookstack.authentication.routes import authentication
    from bookstack.errors.routes import errors
    # Register routes with app
    bookstack.register_blueprint(authentication)
    bookstack.register_blueprint(errors)
    # Return app