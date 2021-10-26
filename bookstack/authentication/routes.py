from flask import (
    Blueprint, Flask, flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from bookstack import mongo

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

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        
        mongo.db.users.insert_one(register)

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
    :param username: username of user
    :return render_template of user_profile.html
    """
    # If no user found = home page
    if 'user' not in session:
        return redirect(url_for("home.html"))
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
    return render_template(
        "user_profile.html", username=session['user'], user=user, 
            books_read=books_read, books_unread=books_unread)


@authentication.route("/logout")
def logout():
    flash("You are logged out.")
    session.pop("user")
    return redirect(url_for("authentication.login"))