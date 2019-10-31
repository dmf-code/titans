# -*- coding: utf-8 -*-
from .base import db


def init(app):
    db.init_app(app)
