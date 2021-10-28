from flask import (
    Blueprint, Flask, flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from bookstack import mongo
from bookstack.util import util

authentication = Blueprint('authentication', __name__)


@authentication.route("/register", methods=["GET", "POST"])
def register():
    """
    This function registers new users as long
    as the username selected is unique
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already taken.")
            return redirect(url_for("authentication.register"))

        # Store img in s3 bucket
        img_path = util.store_image('user_image')

        registered_user = {
            "user_image": img_path,
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registered_user)
        session["user"] = request.form.get("username").lower()
        flash("You are now registered!")

    return render_template("register.html")


@authentication.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back! You're logged in")
            else:
                flash("Whoops! Incorrect username or password.")
                return redirect(url_for("authentication.login"))

        else:
            flash("Whoops! Incorrect username or password.")
            return redirect(url_for("authentication.login"))

    return render_template("login.html")


@authentication.route("/user_profile/<username>", methods=["GET"])
def user_profile(username) -> object:
    """
    This function renders a profile of information
    linked to the logged in user.
    :param username: username of logged in user.
    :return render_template of user_profile.html.
    """
    # If no user found = home page
    if 'user' not in session:
        return redirect(url_for("main.dashboard"))
    user = mongo.db.users.find_one({"username": username})
    # Find docs in collection added by user & read
    books_read = []
    cur = mongo.db.books.find({"added_by": username, "is_read": "yes"})
    for i in cur:
        books_read.append(i)
    books_read = len((books_read))
    # Find docs in collection added by user & unread
    books_unread = []
    cur_unread = mongo.db.books.find({"added_by": username, "is_read": "no"})
    for i in cur_unread:
        books_unread.append(i)
    books_unread = len((books_unread))
    # Find user profile picture
    profile_picture = []
    cur_pic = mongo.db.users.find({"username": username}, {"user_image"})
    for i in cur_pic:
        profile_picture.append(i)
    
    

    return render_template(
        "user_profile.html", username=session['user'], user=user,
            books_read=books_read, books_unread=books_unread,
            profile_picture=profile_picture)


@authentication.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username) -> object:
    """
    This function updates username
    and password of users.
    """
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": username})
        editted_profile = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Update database with user information
        mongo.db.users.update({"username": username}, editted_profile)
        flash(
            "Your profile has been successfully updated, please log back in.")
        session.pop("user")
    user = mongo.db.users.find_one({"username": username})
    return redirect(url_for('authentication.login'))



@authentication.route("/delete_profile/<username>", methods=["GET", "POST"])
def delete_profile(username) -> object:
    """
    This function deletes information
    linked to a user and associated user document
    from the users collection.
    """
    try:
        # Delete challenges added by user
        mongo.db.challenges.delete_many({"added_by": username})
        # Delete reviews added by user
        mongo.db.reviews.delete_many({"added_by": username})
        # Delete books added by user
        mongo.db.books.delete_many({"added_by": username})
        # Delete the user document from the users collection
        mongo.db.users.remove({"username": username})
        # Return to home
        flash("We're sad to see you go! Your account is deleted.")
        session.pop("user")
    except Exception as e:
        flash("An error occurred when trying to delete this profile" + ":" +
              getattr(e, 'message', repr(e)))
    return redirect(url_for('authentication.register'))



@authentication.route("/logout")
def logout() -> object:
    """
    This function logs the user
    from the session
    """
    flash("You are logged out. Come back soon!")
    session.pop("user")
    return redirect(url_for("authentication.login"))