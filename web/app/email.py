from flask_mail import Message
from app import mail
from flask import render_template

no_reply = "admin"


def send_mail(subject, sender, recipients, plain_body, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients, body=plain_body)
    if html_body:
        msg.html = html_body
    mail.send(msg)


def send_password_reset_email(user):
    token = user.generate_token()
    send_mail(
        "Password Reset",
        sender=no_reply,
        recipients=[user.email],
        plain_body=render_template("email/reset_password.txt", user=user, token=token),
        html_body=render_template("email/reset_password.html", user=user, token=token),
    )


def send_confirmation_email(user):
    token = user.generate_token()
    send_mail(
        "Confirm account",
        sender=no_reply,
        recipients=[user.email],
        plain_body=render_template("email/confirm_email.txt", user=user, token=token),
        html_body=render_template("email/confirm_email.html", user=user, token=token),
    )
