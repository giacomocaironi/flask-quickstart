from app import app, db
import click
from app.auth.models import User


@app.cli.group()
def new():
    pass


@create.command()
def admin():
    username = click.prompt("Username")
    email = click.prompt("Email")
    password = click.prompt(
        "Password", hide_input=True, confirmation_prompt="Repeat Password"
    )
    try:
        user = User(username=username, email=email)
        user.set_password(password)
        user.is_admin = True
        db.session.add(user)
        db.session.commit()
    except:
        click.echo("An error has occurred")
