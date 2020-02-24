from app import db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.auth import confirmation_required, admin_required
from app.admin import admin_blueprint
from app.admin.models import *
from app.admin.forms import *

from app.auth.models import User


@admin_blueprint.route("/")
@admin_required
def admin_index():
    return render_template("custom_admin/index.html")


@admin_blueprint.route("/user/<user_id>", methods=["GET", "POST"])
@admin_required
def user_detail(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    form = UserDetail(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("custom_admin.user_detail", user_id=user_id))
    return render_template("custom_admin/user_detail.html", form=form)
