from flask import (render_template, Blueprint)
from progroup import app

errors = Blueprint('errors', __name__)


@app.errorhandler(400)
def error_400(error: object) -> object:
    """
    Render the 400.html template in the case of a 400 error
    (HTTP bad request)
    :return render_template of 400.html
    """
    return render_template('errors/400.html', error=error), 400


@app.errorhandler(401)
def error_401(error: object) -> object:
    """
    Render the 401.html template in the case of a 401 error
    (unauthorized access to a page)
    :return render_template of 401.html
    """
    return render_template('errors/401.html', error=error), 401


@app.errorhandler(404)
def error_404(error: object) -> object:
    """
    Render the 404.html template in the case of a 404 error
    (page not found)
    :return render_template of 404.html
    """
    return render_template('errors/404.html', error=error), 404


@app.errorhandler(405)
def error_405(error: object) -> object:
    """
    Render the 405.html template in the case of a 405 error
    (HTTP method is not allowed)
    :return render_template of 405.html
    """
    return render_template('errors/405.html', error=error), 405


@app.errorhandler(500)
def error_500(error: object) -> object:
    """
    Render the 500.html template in the case of a 500 error
    (internal server error)
    :return render_template of 500.html
    """
    return render_template('errors/500.html', error=error), 500
