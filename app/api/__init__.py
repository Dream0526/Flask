#!/usr/bin/env python3
from flask import Blueprint


api = Blueprint(__name__, 'api', url_prefix='/api/v1.0')

from . import upload, share
