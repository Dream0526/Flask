#!/usr/bin/env python3
from app.models.user_model import FontUser
from datetime import datetime
from app import db


class ShareModel(db.Model):

    __tablename__ = 'shares'
    share_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_id = db.Column(db.String(64), nullable=False)
    # 分享者id
    from_person_id = db.Column(db.String(64), nullable=False)
    from_person_name = db.Column(db.String(64), nullable=False)
    # 被分享者id
    to_person_id = db.Column(db.String(64), nullable=False)
    to_person_name = db.Column(db.String(64), nullable=False)
    share_time = db.Column(db.DateTime(), default=datetime.utcnow)

    @classmethod
    def share_parse(cls, form_data, current_uid):
        """
        to_person_name: 被分享者name，可由前端提供，此处假设前端只提供to_person_id
        current_uid: 分享者id
        """
        to_person_id = form_data.get('to_person_id')
        from_person_id = current_uid.id
        vid = form_data.get('vid')
        to_person = FontUser.query.get_or_404(to_person_id)
        from_person = FontUser.query.get(from_person_id)
        share_obj = cls(
            file_id=vid,
            from_person_id=from_person_id,
            from_person_name=from_person.username,
            to_person_id=to_person_id,
            to_person_name=to_person.username
        )
        db.session.add(share_obj)
        db.session.commit()
        return share_obj

    def object_to_json(self):

        return {
            'share_id': self.share_id,
            'file_id': self.file_id,
            'from_person_name': self.from_person_name,
            'to_person_name': self.to_person_name,
            'share_time': self.share_time
        }

