from flask import (render_template, Blueprint)

from progroup import app
errors = Blueprint('errors', __name__)


@app.errorhandler(400)
def error_404(error: object) -> object:
    """
    Render the 404.html template in the case of a 404 error
    :return render_template of 404.html
    """
    return render_template('errors/404.html', error=error), 400