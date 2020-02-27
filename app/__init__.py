from decouple import config
from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
from flask_bootstrap import Bootstrap

app = Flask(__name__)
if config("DEBUG", default=False, cast=bool):
    config = DevelopmentConfig
else:
    config = ProductionConfig
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "auth.login"
admin_app = Admin(app, name="Flask quickstart", template_mode="bootstrap3")
mail = Mail(app)
bootstrap = Bootstrap(app)

from app.auth import auth_blueprint

app.register_blueprint(auth_blueprint, url_prefix="/auth")

from app.main import main_blueprint

app.register_blueprint(main_blueprint, url_prefix="/")

from app.blog import blog_blueprint

app.register_blueprint(blog_blueprint, url_prefix="/blog")

from app.errors import errors_blueprint

app.register_blueprint(errors_blueprint)
