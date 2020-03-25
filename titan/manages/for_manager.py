# -*- coding: utf-8 -*-
from titan.abstracts.singleton import Singleton
from titan.manages.global_manager import GlobalManager


class ForManager(metaclass=Singleton):

    def __init__(self):
        self.depth = None
        self.for_stack = {}

    def set_depth(self):
        self.depth = GlobalManager().depth

    def set_yield_for_stack(self, func):
        self.for_stack[self.depth] = {
            'yield': func,
            'element': None
        }

    def get_yield_for_stack(self):
        if self.for_stack.get(self.depth, None) is None or self.for_stack[self.depth] is None:
            return None
        return True

    def set_element_for_stack(self, element):
        self.for_stack[self.depth]['element'] = element

    def get_element_for_stack(self):
        return self.for_stack[self.depth]['element']

    def destroy_for_stack(self):
        self.for_stack[self.depth] = None

    def for_loop_start(self):
        if GlobalManager().debug:
            print(self.for_stack)
        element = next(self.for_stack[self.depth]['yield'])
        self.set_element_for_stack(element)
