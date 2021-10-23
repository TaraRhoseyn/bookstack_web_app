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
    return render_template("dashboard.html", books=books)