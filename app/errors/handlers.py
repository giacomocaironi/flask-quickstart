from app.errors import errors_blueprint
from flask import render_template


@errors_blueprint.app_errorhandler(404)
def not_found(error):
    return render_template("errors/404.html"), 404


@errors_blueprint.app_errorhandler(500)
def internal_error(error):
    return render_template("errors/500.html"), 500
