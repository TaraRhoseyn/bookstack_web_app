from flask import (
    Flask, Blueprint, render_template,
    redirect)
from flask_pymongo import PyMongo
from bookstack import mongo

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """
    This function renders the home page
    for users not with an account/logged in
    :return render_template of home.html
    """
    return render_template("home.html")


@main.route("/dashboard")
def dashboard():
    """
    This function renders the main page, dashboard
    :return render_template of dashboard.html
    """
    books = mongo.db.books.find()
    reviews = mongo.db.reviews.find()
    challenges = mongo.db.challenges.find()
    return render_template(
        "dashboard.html", books=books, challenges=challenges
        , reviews=reviews)


@main.route("/review")
def review():
    """
    This function renders the main reviews page
    :return render_template of review.html
    """
    reviews = mongo.db.reviews.find()
    return render_template(
        "review.html", reviews=reviews)


@main.route("/challenge")
def challenge():
    """
    This function renders the main challenges page
    :return render_template of challenge.html
    """
    challenges = mongo.db.challenges.find()
    return render_template(
        "challenge.html", challenges=challenges)


@main.route("/stack")
def stack():
    """
    This function renders the main stacks
    :return render_template of stack.html
    """
    books = mongo.db.books.find()
    return render_template(
        "stack.html", books=books)


@main.route("/contact")
def contact():
    """
    This function renders the contact us page
    :return render_template of contact.html
    """
    return render_template("contact.html")