from flask import (
    Blueprint, Flask, render_template,)


from bookstack import app
errors = Blueprint('errors', __name__)


@app.errorhandler(404)
def error_404(error: object) -> object:
    """
    This function renders the 404.html template
    if a 404 error is triggered.
    :return render_template of 404.html
    """
    return render_template('404.html', error=error), 404