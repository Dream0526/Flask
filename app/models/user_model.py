#!/usr/bin/env python3
from faker import Factory
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.helpers import generate_random_username as gru


class FontUser(db.Model):

    __tablename__ = 'font_user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    username = db.Column(db.String(64), index=True, default=gru)
    _password = db.Column(db.String(256), nullable=False)

    @classmethod
    def create_fake_user(cls, num):
        fake = Factory.create()
        for _ in range(1, num, 1):
            user = FontUser(
                email=fake.email(),
                username=fake.user_name(),
                password='crush'
            )
            db.session.add(user)
        db.session.commit()
        print('{}个用户创建成功'.format(num))

    @property
    def password(self):

        raise AttributeError('access user password is not allowed!')

    @password.setter
    def password(self, pwd):

        self._password = generate_password_hash(pwd)

    def password_verify(self, pwd):

        return check_password_hash(self._password, pwd)
