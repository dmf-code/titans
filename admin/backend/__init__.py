# -*- coding: utf-8 -*-
import os
from flask import Flask


def create_app():
    from . import models, routes, services, templates
    app = Flask(__name__)
    flask_env = os.environ.get('flask_env', None)
    if flask_env:
        if flask_env == 'Production':
            app.config.from_object('admin.backend.configs.ProductionConfig')
        else:
            app.config.from_object('admin.backend.configs.DevelopmentConfig')
    else:
        app.config.from_object('admin.backend.configs.DevelopmentConfig')

    models.init(app)
    routes.init(app)
    services.init(app)
    templates.init(app)

    return app
