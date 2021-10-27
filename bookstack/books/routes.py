from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bookstack import mongo

books = Blueprint('books', __name__)


@books.route("/add_book", methods=["GET", "POST"])
def add_book() -> object:
    """
    This function adds books to the 'books'
    collection and adds reviews to the 'reviews'
    collection.
    :return render_template of add_book.html
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
            "added_by": session["user"],
        }
        mongo.db.reviews.insert_one(book_for_review)
        flash("Book added!")
        return redirect(url_for("main.dashboard"))
    return render_template("add_book.html")


@books.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id) -> object:
    """
    This function uses bson ObjectId
    to pull data from specific document within
    the 'books' collection, then pushes editted
    data back to the collection in the db to be
    updated.
    :return render_template of edit_book.html
    """
    if request.method == "POST":
        is_read = "yes" if request.form.get("read_status") else "no"
        editted_book = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "isbn": request.form.get("isbn"),
            "is_read": is_read,
            "added_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, editted_book)
        flash("Book editted!")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book)


@books.route("/delete_book/<book_id>")
def delete_book(book_id) -> object:
    """
    This function deletes book documents
    from the books collection.
    :return url_for of main.dashboard
    """
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book removed.")
    return redirect(url_for("main.dashboard"))