# -*- coding: utf-8 -*-
from flask import Blueprint
from admin.backend.models.task import Task
from admin.backend.utils import json_response

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/search/<type_>/<name>')
def search(type_, name):
    task = Task.query.filter_by(type=type_, name=name).first()
    return json_response(task.to_json())
