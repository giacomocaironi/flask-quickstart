from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from app.admin.models import *


class UserDetail(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password_hash = StringField("Password", validators=[DataRequired(), Length(min=6)])
    is_admin = BooleanField("admin")
    is_confirmed = BooleanField("confirmed")
    submit = SubmitField("Save")
