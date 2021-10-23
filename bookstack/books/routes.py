from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo

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
            "date_read": request.form.get("date_read"),
        }
    
        if is_read == "yes":
            book_in_stack = {
                "stack_type": "read",
                "created_by": session["user"],
                "book": book
            }
            mongo.db.stacks.insert_one(book_in_stack)
        else:
            book_in_stack = {
                "stack_type": "unread",
                "created_by": session["user"],
                "book": book
            }
            mongo.db.stacks.insert_one(book_in_stack)
            
        mongo.db.books.insert_one(book)
        flash("Book added!")
        return redirect(url_for("main.dashboard"))

    return render_template("add_book.html")