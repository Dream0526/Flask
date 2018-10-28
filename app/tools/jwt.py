#!/usr/bin/env python3
from app.models.user_model import FontUser


def authenticate(username, password):
    user = FontUser.query.filter_by(username=username).first()
    if user and user.password_verify(password):
        return user

def identity(payload):
    user_id = payload['identity']
    return FontUser.query.get(user_id)
