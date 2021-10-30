from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bookstack import mongo

reviews = Blueprint('reviews', __name__)

@reviews.route("/add_review", methods=["GET", "POST"])
def add_review() -> object:
    """
    This function adds reviews to the 'reviews'
    collection.
    :return render_template of add_review.html
    """
    if request.method == "POST":
        review = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "added_by": session["user"],
            "book_review": request.form.get("book_review")
        }
        mongo.db.reviews.insert_one(review)
        flash("Review added!")
        return redirect(url_for("main.dashboard", username=session["user"]))
    return render_template("add_review.html")


@reviews.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id) -> object:
    """
    This function uses bson ObjectId
    to pull data from specific document within
    the 'reviews' collection, then pushes editted
    data back to the collection in the db to be
    updated.
    :return render_template of edit_review.html
    """
    if request.method == "POST":
        editted_review = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "added_by": session["user"],
            "book_review": request.form.get("book_review")
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, editted_review)
        flash("Review editted!")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", reivew=review)


@reviews.route("/delete_review/<review_id>")
def delete_book(review_id) -> object:
    """
    This function deletes review documents
    from the reviews collection.
    :return url_for of main.dashboard
    """
    mongo.db.books.remove({"_id": ObjectId(review_id)})
    flash(
        "Review removed. To remove the book from your stacks, please visit the Stacks page.")
    return redirect(url_for("main.dashboard"))