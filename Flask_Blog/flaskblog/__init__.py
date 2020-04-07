from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    # Create the flask application.
    app = Flask(__name__)

    # Give it the config
    app.config.from_object(Config)

    # initiallize the extension
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Initiallize the blueprints
    from flaskblog.users.routes import users
    app.register_blueprint(users)

    from flaskblog.posts.routes import posts
    app.register_blueprint(posts)

    from flaskblog.main.routes import main
    app.register_blueprint(main)

    return app
