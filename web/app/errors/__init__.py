from flask import Blueprint

errors_blueprint = Blueprint("error", __name__)

from app.errors import handlers
