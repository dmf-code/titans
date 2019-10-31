# -*- coding: utf-8 -*-
from titan.abstracts.singleton import Singleton
from titan.utils import convert_big_hump
from titan import dirs
import importlib
import os


class HookManager(metaclass=Singleton):
    __hook = None

    def __init__(self):
        self.file_name = None
        self.hooks_name = os.listdir(dirs['hooks'])
        print('use hook: ', self.hooks_name)

    def build(self, spider_type):
        self.file_name = spider_type
        if '{}.py'.format(self.file_name) not in self.hooks_name:
            raise Exception('{} is not exist in hooks dir'.format(self.file_name))

        if self.__hook is None:
            load_module = importlib.import_module('titan.hooks.{}'.format(self.file_name))
            print(load_module)
            self.__hook = getattr(load_module, convert_big_hump(self.file_name))

        return self.__hook()


if __name__ == '__main__':
    HookManager().build('common')
