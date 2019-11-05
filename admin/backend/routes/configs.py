# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request
from admin.backend.models.base import db
from admin.backend.models.configs import Configs
from admin.backend.utils import json_response
import json


class ConfigsApi(MethodView):

    def get(self, config_id):
        if config_id is None:
            # 返回一个包含所有用户的列表
            res = []
            configs = Configs.query.all()
            for config in configs:
                res.append(config.to_json())
            return json_response(res)
        else:
            config = Configs.query.filter_by(id=config_id).first()
            return json_response(config.to_json())

    def post(self):
        # 创建一个新用户
        print(request.json)
        json_text = request.json['jsonText']
        if not isinstance(json_text, str):
            json_text = json_text
        db.session.add(Configs(type=request.json['type'], name=request.json['name'], json_text=json_text))
        db.session.commit()

        return json_response()

    def delete(self, config_id):
        # 删除一个用户
        config = Configs.query.filter_by(id=config_id).first()
        db.session.delete(config)
        db.session.commit()
        return json_response()

    def put(self, config_id):
        print(config_id)
        config = Configs.query.filter_by(id=config_id).first()
        config.type = request.json['type']
        config.name = request.json['name']
        config.json_text = json.dumps(request.json['jsonText'])
        print(request.json)
        db.session.commit()
        return json_response()
