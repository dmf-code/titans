# -*- coding: utf-8 -*-
from titan.components import Base
from titan import dirs


class Javascript(Base):
    def default(self):
        if self.driver.execute_script('return typeof jQuery === "undefined";'):
            with open(dirs['storages'] + 'jquery-3.3.1.min.js') as f:
                js = f.read()
            self.driver.execute_script(js)

        exec_script = ''

        if self.params.get('value', None):
            exec_script = 'var selenium_var = "{}";'.format(self.params['value'])

        exec_script = exec_script + self.params['code']
        return self.driver.execute_script(exec_script)
