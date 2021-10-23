import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/dashboard")
def dashboard():
    books = mongo.db.books.find()
    return render_template("dashboard.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    # registers new users if username not taken
    # and no existing users are found
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already taken.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You are now registered!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
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
                return redirect(url_for("login"))

        else:
            flash("Whoops! Incorrect username or password.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/add_book", methods=["GET", "POST"])
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
            "date_read": request.form.get("read_date"),
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
        return redirect(url_for("dashboard"))

    return render_template("add_book.html")


@app.route("/logout")
def logout():
    flash("You are logged out.")
    session.pop("user")
    return redirect(url_for("login"))


# Handles 404 errors. Credit: GeeksForGeeks
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)