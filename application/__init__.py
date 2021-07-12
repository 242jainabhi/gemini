# coding: utf-8
import sys
import os

from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Insert "project root path" to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)


db = SQLAlchemy()
migrate = Migrate()

from application.models import user, workspace, invitation, user_workspace, api_space, env_var, environment, api_endpoint


def create_app():
    """Create Flask app."""
    app = Flask(__name__)
    app.config.from_object(DevConfig())
    db.init_app(app)
    migrate.init_app(app, db)

    # Register components
    return app
