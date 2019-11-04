# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

try:
    db = SQLAlchemy()
except Exception as e:
    db = SQLAlchemy()
