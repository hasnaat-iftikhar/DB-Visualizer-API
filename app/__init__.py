from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# ------------------ Flask App ------------------ #
# Create instances of extensions
# ----------------------------------------------- #

# Creates an instance to connect with the database
db = SQLAlchemy()
# Sets up migration management for the database
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initializing the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints or routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app