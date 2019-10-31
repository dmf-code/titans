# -*- coding: utf-8 -*-
from .base import db


class Task(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    json_text = db.Column(db.Text, nullable=True)

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'name': self.name,
            'jsonText': self.json_text
        }
