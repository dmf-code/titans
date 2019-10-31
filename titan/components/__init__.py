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
            return getattr(self, func_name)()
        else:
            raise Exception('No this function')
