from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from app.admin.models import *


class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password_hash = StringField("Password", validators=[DataRequired(), Length(min=6)])
    is_admin = BooleanField("admin")
    is_confirmed = BooleanField("confirmed")
    submit = SubmitField("Save")


from wtforms_alchemy import ModelForm
from app.auth.models import User


# class UserForm(ModelForm, FlaskForm):
#     class Meta:
#         model = User
#
#     submit = SubmitField("Save")
