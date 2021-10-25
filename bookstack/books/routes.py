from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bookstack import mongo

books = Blueprint('books', __name__)


@books.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        is_read = "yes" if request.form.get("read_status") else "no"
        book = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "isbn": request.form.get("isbn"),
            "is_read": is_read,
            "added_by": session["user"],
            "book_review": request.form.get("book_review"),
        }
    
        mongo.db.books.insert_one(book)
        flash("Book added!")
        return redirect(url_for("main.dashboard"))

    return render_template("add_book.html")