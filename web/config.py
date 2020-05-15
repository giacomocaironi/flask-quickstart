import os
from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = config("SECRET_KEY", default="hgdk;4lAgjadkls;AEGs")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_HTTPONLY = True
    NAME = config("NAME", default="")
    MAIL_SERVER = config("MAIL_SERVER", default="localhost")
    MAIL_PORT = config("MAIL_PORT", default=8025, cast=int)
    MAIL_USERNAME = config("MAIL_USERNAME", default="")
    MAIL_PASSWORD = config("MAIL_PASSWORD", default="")
    DEBUG = False
    TESTING = False

    # uploads
    UPLOADED_DOCUMENTS_URL = "/upload/documents/"
    UPLOADED_IMAGES_URL = "/uploads/images/"
    UPLOADED_IMAGES_DEST = config("UPLOADED_IMAGES_DEST")
    UPLOADED_DOCUMENTS_DEST = config("UPLOADED_DOCUMENTS_DEST")


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = config(
        "DATABASE_URL", default="sqlite:///" + os.path.join(basedir, "development.db")
    )
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = config(
        "DATABASE_URL", default="sqlite:///" + os.path.join(basedir, "production.db")
    )
    MAIL_USE_TLS = 1
    # remember to setup https or the site won't work
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
