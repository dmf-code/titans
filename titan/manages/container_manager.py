# -*- coding: utf-8 -*-
from titan.abstracts.singleton import Singleton
from titan.utils import convert_big_hump
from titan import dirs
import importlib
import os


class ContainerManager(metaclass=Singleton):
    __contains = {}

    def __init__(self):
        self.components_name = os.listdir(dirs['components'])
        # print(self.components_name)

    def build(self, module, args=None):
        if '{}.py'.format(module) not in self.components_name:
            raise Exception('{} is not exist in components dir'.format(module))
        if module not in self.__contains:
            load_module = importlib.import_module('titan.components.{}'.format(module))
            # print(load_module)
            self.__contains[module] = getattr(load_module, convert_big_hump(module))

        # print(self.__contains)
        if args is None:
            instance = self.__contains[module]()
        else:
            instance = self.__contains[module](args)
        return instance


if __name__ == '__main__':
    factory = ContainerManager()
    factory.build('click')
