from app import app, db
import click
from app.auth.models import User
import os, sys
import jinja2
from jinja2 import Template


@app.cli.group()
def new():
    pass


@new.command()
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


@new.command()
@click.argument("name")
def module(name):
    if os.path.isdir(os.path.join("app", name)):
        click.echo("A module named like this alrealdy exist")
        return
    if os.path.isdir(os.path.join("app", "templates", name)):
        click.echo("A template submodule named like this alrealdy exist")
        return
    os.mkdir(os.path.join("app", name))
    os.mkdir(os.path.join("app", "templates", name))
    for file in os.listdir(os.path.join("utilities", "base_module")):
        with open(os.path.join("utilities", "base_module", file), "r") as raw:
            if file == "index.html":
                rendered_file = (
                    """{% extends "base.html" %}
{% block content %}
<h1>"""
                    + name
                    + """</h1>
{% endblock content %}
                """
                )
                with open(
                    os.path.join("app", "templates", name, file), "w"
                ) as new_file:
                    new_file.write(rendered_file)
            else:
                rendered_file = Template(raw.read()).render(name=name)
                with open(os.path.join("app", name, file), "w") as new_file:
                    new_file.write(rendered_file)
