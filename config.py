import os
from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = config("SECRET_KEY", default="hgdk;4lAgjadkls;AEGs")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = config("LOG_TO_STDOUT")
    REMEMBER_COOKIE_HTTPONLY = True
    ADMINS = config("AMINS", default="").split(", ")


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = config(
        "DATABASE_URL", default="sqlite:///" + os.path.join(basedir, "development.db")
    )


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = config(
        "DATABASE_URL", default="sqlite:///" + os.path.join(basedir, "production.db")
    )
