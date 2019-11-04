# -*- coding: utf-8 -*-
from admin.backend import create_app, init_app

app = create_app()

init_app(app)

app.run()
