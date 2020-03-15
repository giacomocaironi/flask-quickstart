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


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = config(
        "DATABASE_URL", default="sqlite:///" + os.path.join(basedir, "development.db")
    )


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = config(
        "DATABASE_URL", default="sqlite:///" + os.path.join(basedir, "production.db")
    )
    MAIL_USE_TLS = 1
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
