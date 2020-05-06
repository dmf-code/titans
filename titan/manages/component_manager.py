# -*- coding: utf-8 -*-
from titan.abstracts.singleton import Singleton
from titan.utils import convert_big_hump
from titan import dirs
import importlib
import os, re


class ComponentManager(metaclass=Singleton):
    __contains = {}

    def recursive_dir(self, path, prefix="", result=[]):
        path = path.rstrip(os.path.sep) + os.path.sep
        for p in os.listdir(path):
            if os.path.isfile(path + p):
                if prefix is "":
                    result.append(p)
                else:
                    result.append(prefix + p)
            else:
                self.recursive_dir(path + p, prefix + p + ".", result)

        result = list(filter(lambda x: re.match("\S+.py$", x), result))
        return result

    def __init__(self):
        self.components_name = self.recursive_dir(dirs['components'])

    def build(self, module, args=None):
        if '{}.py'.format(module) not in self.components_name:
            raise Exception('{} is not exist in components dir'.format(module))
        if module not in self.__contains:
            load_module = importlib.import_module('titan.components.{}'.format(module))
            ins = module.split('.')[-1]
            self.__contains[module] = getattr(load_module, convert_big_hump(ins))

        if args is None:
            instance = self.__contains[module]()
        else:
            instance = self.__contains[module](args)
        return instance


if __name__ == '__main__':
    factory = ComponentManager()
    factory.build('click')
