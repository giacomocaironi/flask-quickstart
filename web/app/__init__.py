from flask import Flask
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
from flask_paranoid import Paranoid
from flask_pagedown import PageDown
from flaskext.markdown import Markdown
from flask_uploads import (
    UploadSet,
    IMAGES,
    DOCUMENTS,
    configure_uploads,
    patch_request_class,
)


app = Flask(__name__)
if app.config["ENV"] == "development":
    app.config.from_object(DevelopmentConfig)
elif app.config["ENV"] == "testing":
    app.config.from_object(TestingConfig)
elif app.config["ENV"] == "production":
    app.config.from_object(ProductionConfig)
else:
    print("Unkown configuration name")
    raise
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "auth.login"
admin_app = Admin(
    app,
    name="Flask quickstart",
    template_mode="bootstrap3",
    base_template="admin/my_base.html",
)
mail = Mail(app)
paranoid = Paranoid(app)
paranoid.redirect_view = "main.index"

# blog related
pagedown = PageDown(app)
markdown = Markdown(app)

# upload related
images = UploadSet("images", IMAGES)
documents = UploadSet("documents", DOCUMENTS)
configure_uploads(app, (images, documents))
patch_request_class(app, 16 * 1024 * 1024)

from app.auth import auth_blueprint

app.register_blueprint(auth_blueprint, url_prefix="/auth")

from app.errors import errors_blueprint

app.register_blueprint(errors_blueprint)

from app.main import main_blueprint

app.register_blueprint(main_blueprint, url_prefix="/")

from app.blog import blog_blueprint

app.register_blueprint(blog_blueprint, url_prefix="/blog")

from app.uploads import *
