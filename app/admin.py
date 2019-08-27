from flask import redirect, url_for, request
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from app import app, db, admin_app
from app.auth.models import User


class AdminModelView(ModelView):
    def is_accessible(self):
        return (
            current_user.is_authenticated
            and current_user.username in app.config["ADMINS"]
        )

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("login", next=request.url))


admin_app.add_view(AdminModelView(User, db.session))
