#!/usr/bin/env python3
from flask import request, jsonify
from flask_jwt import current_identity
from . import api


@api.route('/share/<receiver>/', methods=['POST'])
def share(receiver):
    """
    文件分享
    receiver: 被分享者id
    """
    pass
