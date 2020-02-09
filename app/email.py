from flask_mail import Message
from app import mail


def send_mail(subject, sender, recipients, plain_body, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients, body=plain_body)
    if html_body:
        msg.html = html_body
    mail.send(msg)
