# -*- coding: utf-8 -*-
from titan.manages.global_manager import GlobalManager
from titan.abstracts.decorator import run_time_sum
import time


class Base(object):
    allow = True

    def __init__(self, params):
        self.driver = GlobalManager().get_driver()
        self.params = params

    @staticmethod
    def sleep(sleep_time=5):
        time.sleep(sleep_time)

    @run_time_sum
    def run(self, func_name):
        print('func_name: ', func_name)
        if hasattr(self, func_name) and (self.allow or func_name in self.allow):
            result = getattr(self, func_name)()
            if self.params.get('sleep_time', None):
                self.sleep(self.params['sleep_time'])
            return result
        else:
            raise Exception('No this function')
