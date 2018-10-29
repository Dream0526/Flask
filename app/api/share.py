#!/usr/bin/env python3
from flask import request, jsonify, abort
from flask_jwt import current_identity, jwt_required
from app.models.share_model import ShareModel
from . import api


@api.route('/share/', methods=['POST'])
@jwt_required()
def share():
    """
    文件分享
    receiver: 被分享者id
    """
    share_obj = ShareModel.share_parse(request.form, current_identity)
    return jsonify(share_obj.object_to_json())
