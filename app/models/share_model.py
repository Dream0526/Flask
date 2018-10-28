#!/usr/bin/env python3
from datetime import datetime
from app import db


class ShareModel(db.Model):

    __tablename__ = 'shares'
    share_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_id = db.Column(db.String(64), nullable=False)
    # 分享者id
    from_person = db.Column(db.String(64), nullable=False)
    # 被分享者id
    to_person = db.Column(db.String(64), nullable=False)
    share_time = db.Column(db.DateTime(), default=datetime.utcnow)
