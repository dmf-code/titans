# -*- coding: utf-8 -*-
from .base import db


class Tasks(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False)
    type = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    result = db.Column(db.JSON, nullable=True)

    def to_json(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'type': self.type,
            'name': self.name,
            'result': self.result
        }
