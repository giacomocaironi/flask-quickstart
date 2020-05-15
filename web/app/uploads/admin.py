from flask import redirect, url_for, request, current_app
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from app import db, admin_app
from app.uploads.models import *
from flask_admin import form
import os
import uuid
from werkzeug.utils import secure_filename
from decouple import config


def _imagename_uuid1_gen(obj, file_data):
    _, ext = os.path.splitext(file_data.filename)
    uid = uuid.uuid1()
    return secure_filename("{}{}".format(uid, ext))


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("login", next=request.url))


class DocumentView(AdminModelView):

    form_extra_fields = {
        "filename": form.FileUploadField(
            "Image",
            base_path=config("UPLOADED_DOCUMENTS_DEST"),
            namegen=_imagename_uuid1_gen,
        )
    }


class ImageView(AdminModelView):

    form_extra_fields = {
        "filename": form.ImageUploadField(
            "Image",
            base_path=config("UPLOADED_IMAGES_DEST"),
            url_relative_path="images/",
            namegen=_imagename_uuid1_gen,
        )
    }


admin_app.add_view(ImageView(Image, db.session, category="Uploads"))
admin_app.add_view(DocumentView(Document, db.session, category="Uploads"))
