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


@authentication.route("/logout")
def logout():
    flash("You are logged out.")
    session.pop("user")
    return redirect(url_for("authentication.login"))