# -*- coding: utf-8 -*-
import json


def json_response(data='', code=0, msg='success'):
    return {'code': code, 'data': data, 'msg': msg}
