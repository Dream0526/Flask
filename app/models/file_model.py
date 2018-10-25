#!/usr/bin/env python3
from flask import current_app
from datetime import datetime
import shortuuid
import os
from app import db


class InstanceFile(db.Model):
    """
    所上传的真实文件
    """
    __tablename__ = 'instance_file'
    fid = db.Column(db.String(32), primary_key=True)
    fmd5 = db.Column(db.String(32), unique=True, nullable=False)
    server_path = db.Column(db.String(256), nullable=False)
    upload_time = db.Column(db.DateTime(), default=datetime.utcnow)

    @classmethod
    def file_exist(cls, md5_val):

        query_result = cls.query.filter_by(fmd5=md5_val).first()
        return True if query_result else False

    @classmethod
    def create_instance_file(cls, file, md5_val):
        """
        将用户上传的文件保存到指定目录
        """
        abs_path = os.path.join(current_app.config['UPLOAD_FILE_REPOSITORY'], file.filename)
        file.save(abs_path)
        instance_file = cls(
            fid=shortuuid.uuid(),
            fmd5=md5_val,
            server_path=abs_path
        )
        db.session.add(instance_file)
        db.session.commit()
        return instance_file

    def object_to_json(self):

        json_file =  {
            'fid': self.fid,
            'fmd5': self.fmd5,
            'server_path': self.server_path,
            'upload_time': self.upload_time
        }
        return json_file


class VirtualFile(db.Model):

    __tablename__ = 'virtual_file'
    vid = db.Column(db.Integer, primary_key=True)
    # 和实体文件表中文件的关联
    instance_id = db.Column(db.String(32), db.ForeignKey('instance_file.fid'))
    # 该虚拟文件所属者的id
    owner_id = db.Column(db.Integer, db.ForeignKey('font_user.uid'))
    fmd5 = db.Column(db.String(32), nullable=False)
    # 前端展示出来的文件路径，也是用户寻找到文件的唯一方式
    client_path = db.Column(db.Text, nullable=False)
    # 在服务器上保存的后的文件路径
    server_path = db.Column(db.String(256), nullable=False)
    # 前端展示出的文件名
    font_file_name = db.Column(db.String(256), nullable=False)
    # 在服务器上保存后的文件名
    server_filename = db.Column(db.String(256), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    file_type = db.Column(db.String(16), default=u'未知文件类型')
    upload_time = db.Column(db.DateTime(), default=datetime.utcnow)

    @classmethod
    def create_virtual_file(cls, file_info, owner_id):

        pass
