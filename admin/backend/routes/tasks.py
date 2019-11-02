# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request
from admin.backend.models.base import db
from admin.backend.models.task import Task
from admin.backend.utils import json_response
import json


class TasksApi(MethodView):

    def get(self, task_id):
        if task_id is None:
            # 返回一个包含所有用户的列表
            res = []
            tasks = Task.query.all()
            for task in tasks:
                res.append(task.to_json())
            return json_response(res)
        else:
            # 显示一个用户
            pass

    def post(self):
        # 创建一个新用户
        print(request.json)
        json_text = request.json['jsonText']
        if isinstance(json_text, dict):
            json_text = json.dumps(json_text)
        db.session.add(Task(type=request.json['type'], name=request.json['name'], json_text=json_text))
        db.session.commit()

        return {'status': 'success'}

    def delete(self, task_id):
        # 删除一个用户
        task = Task.query.filter_by(id=task_id).first()
        db.session.delete(task)
        db.session.commit()
        return {'status': 'success'}

    def put(self, task_id):
        # update a single user
        print(task_id)
        task = Task.query.filter_by(id=task_id).first()
        task.type = request.json['type']
        task.name = request.json['name']
        task.json_text = json.dumps(request.json['jsonText'])
        print(request.json)
        db.session.commit()
        return {'status': 'success'}
