from flask import Blueprint

blog_blueprint = Blueprint("blog", __name__)

from app.blog import forms, models, views, admin
