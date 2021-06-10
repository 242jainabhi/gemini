# coding: utf-8
import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)
import logging
from flask import Flask
from config import DevConfig


def create_app():
    """Create Flask app."""
    app = Flask(__name__)
    app.config.from_object(DevConfig())

    # Register components
    return app