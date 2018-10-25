#!/usr/bin/env python3
from flask import request, jsonify
from app.helpers import calculate_md5_for_bigfile
from app.models.file_model import InstanceFile, VirtualFile
from . import api


@api.route('/upload_file/', methods=['POST'])
def upload_file():

    get_file = request.files.get('file')
    uploader_id = request.args.get('uploader')
    file_md5 = calculate_md5_for_bigfile(get_file)
    # 如果该文件没有被上传过，则保存该文件，并写到instance_file表中
    if not InstanceFile.file_exist(file_md5):
        f = InstanceFile.create_instance_file(get_file, file_md5)
    else:
        f = InstanceFile.query.filter_by(fmd5=file_md5).first()
        print('exists')
    # VirtualFile.create_virtual_file(file_info, uploader_id)
    return jsonify({'status': 2000})

