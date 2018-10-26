#!/usr/bin/env python3
import werkzeug
from flask import request, jsonify, current_app
from app.helpers import calculate_md5_for_bigfile
from app.models.file_model import InstanceFile, VirtualFile
from . import api
from app import db


@api.route('/upload_file/', methods=['POST'])
def upload_file():

    get_file = request.files.get('file')
    uploader_id = request.form.get('uploader')
    file_md5 = calculate_md5_for_bigfile(get_file)
    # 如果该文件没有被上传过，则保存该文件，并写到instance_file表中
    if not InstanceFile.file_exist(file_md5):
        instance = InstanceFile.create_instance_file(get_file, file_md5)
    else:
        instance = InstanceFile.query.filter_by(fmd5=file_md5).first()
    file_info = instance.object_to_json()
    virtual = VirtualFile.create_virtual_file(file_info, uploader_id)
    try:
        db.session.add_all([instance, virtual])
        db.session.commit()
        get_file.save(file_info.get('server_path'))
        return jsonify({'status': 200})
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'status': 100})
