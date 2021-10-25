from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bookstack import mongo

books = Blueprint('books', __name__)


@books.route("/add_book", methods=["GET", "POST"])
def add_book():
    """
    This function adds books to the 'books'
    collection and adds reviews to the 'reviews'
    collection.
    """
    if request.method == "POST":
        is_read = "yes" if request.form.get("read_status") else "no"
        book = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "isbn": request.form.get("isbn"),
            "is_read": is_read,
            "added_by": session["user"],
        }
        mongo.db.books.insert_one(book)
        book_for_review = {
            "book_review": request.form.get("book_review"),
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "written_by": session["user"],
        }
        mongo.db.reviews.insert_one(book_for_review)
        flash("Book added!")
        return redirect(url_for("main.dashboard"))
    return render_template("add_book.html")


@books.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book)