#!/usr/bin/env python3
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.helpers import generate_random_username as gru


class FontUser(db.Model):

    __tablename__ = 'font_user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    username = db.Column(db.String(16), index=True, default=gru)
    authoriation = db.Column(db.String(256))
    _password = db.Column(db.String(256), nullable=False)

    @property
    def password(self):

        raise AttributeError('access user password is not allowed!')

    @password.setter
    def password(self, pwd):

        self._password = generate_password_hash(pwd)

    def password_verify(self, pwd):

        return check_password_hash(self._password, pwd)
