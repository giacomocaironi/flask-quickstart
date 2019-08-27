from flask import Blueprint

base_blueprint = Blueprint("base", __name__)

from app.base import forms, models, views
