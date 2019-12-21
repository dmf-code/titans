# -*- coding: utf-8 -*-
from titan.abstracts.singleton import Singleton
from titan import YAML_CONFIG
import re


class GlobalManager(metaclass=Singleton):

    def __init__(self):
        self._instances = {}
        self._storage = {}
        self._system = {}
        self._db_args = {}
        self.for_stack = {}
        self.depth = 0
        self.is_if = False
        self.is_break = False
        self.is_loop = True
        self.driver = None
        self.component_name = None
        self.component_type = None
        self.debug = YAML_CONFIG['debug']

    def set_driver(self, driver):
        if self.driver is None:
            self.driver = driver
        return self.driver

    def get_driver(self):
        return self.driver

    def loop_turn_on(self):
        self.is_loop = True

    def loop_turn_off(self):
        self.is_loop = False

    def break_turn_on(self):
        self.is_break = True

    def break_turn_off(self):
        self.is_break = False

    def if_turn_on(self):
        self.is_if = True

    def if_turn_off(self):
        self.is_if = False

    def build(self, spider_type, task_name, uuid):
        self._system['spider_type'] = spider_type
        self._system['task_name'] = task_name
        self._system['uuid'] = uuid

    def set(self, keys, value, type_='_storage'):
        data = getattr(self, type_, None)
        if data is None:
            raise Exception('not have type: {}'.format(type_))
        key_list = keys.split('.')
        # len(key_list) > 1 and key_list.reverse()

        while len(key_list) > 1:
            key = key_list.pop()
            if key not in data:
                data[key] = {}
            data = data[key]

        key = key_list.pop()
        if re.search('_custom_array', key):
            if key not in data or not isinstance(data[key], list):
                data[key] = []
            data[key].append(value)
        else:
            data[key] = value

    def get(self, keys=None, type_='_storage'):
        value = getattr(self, type_, {})

        if keys is None:
            return value

        if not isinstance(keys, str):
            raise Exception('key must be str')
        _keys = keys.split('.')
        for _key in _keys:
            value = value.get(_key, None)
            if not value:
                break
        return value
