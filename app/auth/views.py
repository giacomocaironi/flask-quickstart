from app import db
from app.auth import auth_blueprint
from flask import render_template, flash, redirect, url_for, request
from app.auth.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.auth.forms import *
from app.email import *


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(
            form.password.data
        ):  # can validate also in the form itself
            flash("invalid username or password")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        destination = request.args.get("next")
        if not destination or url_parse(destination).netloc != "":
            return redirect(url_for("main.index"))
        return redirect(destination)
    return render_template("auth/login.html", form=form)


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("auth.request_confirmation_email"))
    return render_template("auth/register.html", form=form)


@auth_blueprint.route("/confirm", methods=["GET"])
@login_required
def request_confirmation_email():
    if current_user.is_confirmed:
        return redirect(url_for("main.index"))
    send_confirmation_email(current_user)
    return redirect(url_for("auth.unconfirmed"))


@auth_blueprint.route("/unconfirmed", methods=["GET"])
@login_required
def unconfirmed():
    if current_user.is_confirmed:
        return redirect(url_for("main.index"))
    return render_template("auth/unconfirmed.html")


@auth_blueprint.route("/confirm/<token>", methods=["GET"])
def confirm_account(token):
    if current_user.is_authenticated:
        if current_user.is_confirmed:
            return redirect(url_for("main.index"))
    user = User.verify_token(token)
    if not user:
        return redirect(url_for("main.index"))
    try:
        user.is_confirmed = True
        db.session.commit()
        logout_user()
    except Exception as e:
        db.session.rollback()
    return redirect(url_for("main.index"))


@auth_blueprint.route("/reset", methods=["GET", "POST"])
def request_password_reset():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RequestPasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash("Check your email to reset your password")
        return redirect(url_for("auth.login"))
    return render_template("auth/request_password_reset.html", form=form)


@auth_blueprint.route("/reset/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = ResetPasswordForm()
    user = User.verify_token(token)
    if not user:
        return redirect(url_for("main.index"))
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password.html", form=form)
