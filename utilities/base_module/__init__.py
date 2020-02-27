from flask import Blueprint

{{name}}_blueprint = Blueprint("{{name}}", __name__)

from app.{{name}} import forms, models, views, admin
