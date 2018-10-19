#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configs


db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(Configs[config_name])
    db.init_app(app)

    return app
