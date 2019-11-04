# -*- coding: utf-8 -*-
import os
from flask import Flask
from admin.backend.bule_print import api


def create_app():
    app = Flask(__name__)
    flask_env = os.environ.get('flask_env', None)
    if flask_env:
        if flask_env == 'Production':
            app.config.from_object('admin.backend.configs.ProductionConfig')
        else:
            app.config.from_object('admin.backend.configs.DevelopmentConfig')
    else:
        app.config.from_object('admin.backend.configs.DevelopmentConfig')

    app.register_blueprint(api)

    return app


def init_app(app):
    from . import models, routes, services, templates
    models.init(app)
    routes.init(app)
    services.init(app)
    templates.init(app)
