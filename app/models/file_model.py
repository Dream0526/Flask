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
    # 文件上传时候的路径
    origin_path = db.Column(db.String(256), nullable=False)
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
        instance_file = cls(
            fid=shortuuid.uuid(),
            fmd5=md5_val,
            server_path=abs_path
        )
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
    vid = db.Column(db.String(32), primary_key=True)
    # 和实体文件表中文件的关联
    instance_id = db.Column(db.String(32), db.ForeignKey('instance_file.fid'))
    # 该虚拟文件所属者的id
    owner_id = db.Column(db.Integer, db.ForeignKey('font_user.id'))
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

    @staticmethod
    def rename(origin_name, num):
        name_list = origin_name.split('.')
        new_name = '.'.join(name_list[:-1]) + '({}).'.format(num) + name_list[-1]
        return new_name

    @classmethod
    def create_virtual_file(cls, file_info, owner_id, file):
        """
        file_size, file_type, client_path 均由前端提供
        """
        query_result = cls.query.filter(cls.owner_id==owner_id, cls.server_filename==file.filename)
        if query_result:
            font_file_name = cls.rename(file.filename, query_result.count())
        else:
            font_file_name = file.filename
        virtual = cls(
            vid=shortuuid.uuid(),
            instance_id=file_info.get('fid'),
            owner_id=owner_id,
            fmd5=file_info.get('fmd5'),
            client_path='client_path',
            server_path=file_info.get('server_path'),
            font_file_name=font_file_name,
            server_filename=file.filename,
            file_size=1024,
            file_type='png',
            upload_time=file_info.get('uplod_time')
        )
        return virtual

    def object_to_json(self):

        return {
            'vid': self.vid,
            'instance_id': self.instance_id,
            'owner_id': self.owner_id,
            'fmd5': self.fmd5,
            'client_path': self.client_path,
            'server_path': self.server_path,
            'font_file_name': self.font_file_name,
            'server_file_name': self.server_filename,
            'file_size': self.file_size,
            'file_type': self.file_type,
            'upload_time': self.upload_time
        }
