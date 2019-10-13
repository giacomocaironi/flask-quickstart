from app import app, db
import click
from app.auth.models import User


@app.cli.group()
def create():
    pass


@create.command()
def superuser():
    username = input("username: ")
    email = input("email: ")
    password = input("password: ")
    user = User(username=username, email=email)
    user.set_password(password)
    user.is_admin = True
    db.session.add(user)
    db.session.commit()
