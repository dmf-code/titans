# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request
from admin.backend.models.base import db
from admin.backend.models.task import Task
from admin.backend.utils import json_response


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
        db.session.add(Task(type=request.json['type'], name=request.json['name'], json_text=request.json['jsonText']))
        db.session.commit()

        return {'status': 'success'}

    def delete(self, task_id):
        # 删除一个用户
        pass

    def put(self, task_id):
        # update a single user
        pass
