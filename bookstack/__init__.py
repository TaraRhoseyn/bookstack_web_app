import os
from flask import (Flask)
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
mongo.init_app(app)

def create_app():
    """
    Initialize the app with blueprint routes
    """
    # Import blueprint routes
    from bookstack.authentication.routes import authentication
    from bookstack.errors.routes import errors
    from bookstack.books.routes import books
    from bookstack.main.routes import main
    from bookstack.reviews.routes import reviews
    from bookstack.challenges.routes import challenges
    # Register routes with app
    app.register_blueprint(authentication)
    app.register_blueprint(errors)
    app.register_blueprint(books)
    app.register_blueprint(reviews)
    app.register_blueprint(challenges)
    app.register_blueprint(main)
    # Return app
    return app