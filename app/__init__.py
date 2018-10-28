#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
from config import Configs


db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(Configs[config_name])
    db.init_app(app)

    from app.tools.jwt import authenticate, identity
    jwt = JWT(app, authenticate, identity)

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
