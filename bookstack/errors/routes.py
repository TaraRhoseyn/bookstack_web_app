from flask import (
    Blueprint, Flask, render_template,)

errors = Blueprint('errors', __name__)


@errors.errorhandler(404)
def not_found(e):
    """
    This function renders the 404.html template
    if a 404 error is triggered.
    :return render_template of 404.html
    """
    return render_template("404.html")