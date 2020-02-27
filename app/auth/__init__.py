from flask import Blueprint, redirect, url_for
from functools import wraps
from flask_login import current_user

auth_blueprint = Blueprint("auth", __name__)


def confirmation_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.is_confirmed:
            return redirect(url_for("auth.unconfirmed"))
        return func(*args, **kwargs)

    return decorated_function


def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)

    return decorated_function


from app.auth import forms, models, views, admin
