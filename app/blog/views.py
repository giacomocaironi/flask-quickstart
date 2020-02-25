from app import db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.auth import confirmation_required
from app.blog import blog_blueprint
from app.blog.models import *
from app.blog.forms import *


@blog_blueprint.route("/", methods=["GET"])
@login_required
@confirmation_required
def index():
    return render_template("blog/index.html", context={})
