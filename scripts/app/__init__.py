import os
from flask import Flask
from app.config import config


def create_app(test_mode=False):
    """ Create flask application instance """
    app = Flask(__name__)
    if test_mode:
        app.config.from_object(config["test"])
    else:
        env = os.environ.get("FLASK_ENV", "dev")
        app.config.from_object(config[env])

    return app
