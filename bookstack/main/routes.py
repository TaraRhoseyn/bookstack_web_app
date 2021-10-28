from flask import (
    Flask, Blueprint, render_template,
    redirect)
from flask_pymongo import PyMongo
from bookstack import mongo

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/dashboard")
def dashboard():
    books = mongo.db.books.find()
    reviews = mongo.db.reviews.find()
    return render_template(
        "dashboard.html", books=books, reviews=reviews)


@main.route("/contact")
def contact():
    return render_template("contact.html")