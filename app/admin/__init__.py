from flask import Blueprint

admin_blueprint = Blueprint("admin", __name__)

from app.admin import forms, models, views
