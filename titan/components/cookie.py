# -*- coding: utf-8 -*-
from titan.components import Base
from titan import dirs
import json
import os


class Cookie(Base):
    def write_file(self):
        cookie = self.driver.get_cookies()
        path = dirs['cookies'] + self.params['cookie_name'] + '.txt'
        with open(path, 'w') as f:
            json.dump(cookie, f)

        return path
