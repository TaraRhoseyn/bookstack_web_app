from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bookstack import mongo

challenges = Blueprint('challenges', __name__)


@challenges.route("/add_challenge", methods=["GET", "POST"])
def add_challenge() -> object:
    """
    This function adds challenges to the 'challenges'
    collection.
    :return render_template of add_challenge.html
    """
    if request.method == "POST":
        challenge = {
            "challenge_name": request.form.get("challenge_name"),
            "added_by": session["user"],
            "is_complete": "no"
        }
        mongo.db.challenges.insert_one(challenge)
        flash("Challenge added!")
        return redirect(url_for("main.dashboard", username=session["user"]))
    return render_template("add_challenge.html")


@challenges.route("/edit_challenge/<challenge_id>", methods=["GET", "POST"])
def edit_challenge(challenge_id) -> object:
    """
    This function uses bson ObjectId
    to pull data from specific document within
    the 'challenges' collection, then pushes editted
    data back to the collection in the db to be
    updated.
    :return render_template of edit_challenge.html
    """
    if request.method == "POST":
        is_complete = "yes" if request.form.get("complete_status") else "no"
        editted_challenge = {
            "challenge_name": request.form.get("challenge_name"),
            "added_by": session["user"],
            "is_complete": is_complete
        }
        mongo.db.challenges.update(
            {"_id": ObjectId(challenge_id)}, editted_challenge)
        flash("challenge editted!")

    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    return render_template("edit_challenge.html", challenge=challenge)


@challenges.route("/delete_challenge/<challenge_id>")
def delete_challenge(challenge_id) -> object:
    """
    This function deletes challenge documents
    from the challenges collection.
    :return url_for of main.dashboard
    """
    mongo.db.challenges.remove({"_id": ObjectId(challenge_id)})
    flash(
        "Challenge removed. To remove book, please visit Stacks.")
    return redirect(url_for("main.dashboard"))
