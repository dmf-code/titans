# -*- coding: utf-8 -*-
from flask import Blueprint
from admin.backend.models.task import Task
from admin.backend.utils import json_response
from flask import request

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/search/<type_>/<name>')
def search(type_, name):
    task = Task.query.filter_by(type=type_, name=name).first()
    return json_response(task.to_json())


@api.route('/callback', methods=['POST'])
def callback():
    print(request.form)
    print(request.json)
    return json_response()
