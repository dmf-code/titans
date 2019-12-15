# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request
from admin.backend.models.base import db
from admin.backend.models.tasks import Tasks
from admin.backend.utils import json_response
import json


class TasksApi(MethodView):

    def get(self, task_id):
        if task_id is None:
            # 返回一个包含所有用户的列表
            res = []
            tasks = Tasks.query.all()
            for config in tasks:
                res.append(config.to_json())
            return json_response(res)
        else:
            config = Tasks.query.filter_by(id=task_id).first()
            return json_response(config.to_json())

    def post(self):
        # 创建一个新用户
        print(request.json)
        db.session.add(
            Tasks(
                type=request.json['type'],
                uuid=request.json['uuid'],
                name=request.json['name'],
                result=request.json['result']
            )
        )
        db.session.commit()

        return json_response()

    def delete(self, task_id):
        # 删除一个用户
        config = Tasks.query.filter_by(id=task_id).first()
        db.session.delete(config)
        db.session.commit()
        return json_response()

    def put(self, task_id):
        print(task_id)
        config = Tasks.query.filter_by(id=task_id).first()
        config.type = request.json['type']
        config.name = request.json['name']
        config.json_text = json.dumps(request.json['result'])
        print(request.json)
        db.session.commit()
        return json_response()
