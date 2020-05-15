from flask import redirect, url_for, request
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from app import db, admin_app
from app.blog.models import *
from flask_pagedown.fields import PageDownField


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("login", next=request.url))


class PostView(AdminModelView):

    form_extra_fields = {"content": PageDownField()}


admin_app.add_view(PostView(Post, db.session, category="Blog"))
admin_app.add_view(AdminModelView(Category, db.session, category="Blog"))
admin_app.add_view(AdminModelView(Tag, db.session, category="Blog"))
