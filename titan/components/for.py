# -*- coding: utf-8 -*-
from titan.components import Base
from titan.manages.global_manager import GlobalManager
from titan.manages.for_manager import ForManager
from titan.utils import screening_value
import traceback
import copy


class For(Base):
    __stack = {}

    def __init__(self, params):
        super(For, self).__init__(params)
        ForManager().set_depth()
        if GlobalManager().component_type == 'start' and ForManager().get_yield_for_stack() is None:
            ForManager().set_yield_for_stack(self.loop_condition())

    def loop_condition(self):
        elements = []

        if self.params.get('xpath', None):
            elements = self.driver.find_elements_by_xpath(self.params['xpath'])

        if self.params.get('value', None):
            elements = self.params['value']

        if self.params.get('storage', None):
            elements = GlobalManager().get(self.params['storage'])

        for element in elements:
            yield element

    def click(self):
        if self.params.get('xpath', None):
            text = None
            if self.params.get('format', None):
                text = self.params['format'].format(**ForManager().get_element_for_stack())
            xpath = self.params['xpath'].format(text)
            self.driver.find_element_by_xpath(xpath).click()

    def grab(self):
        element = ForManager().get_element_for_stack()

        if self.params.get('xpath', None):
            element = element.find_element_by_xpath(self.params['xpath'])

        if self.params.get('tag_name', None):
            element = element.find_element_by_tag_name(self.params['tag_name'])

        if GlobalManager().debug:
            print(element.text)

        self.__stack[self.params['key']] = screening_value(element, self.params)

    def start(self):
        try:
            ForManager().for_loop_start()
        except Exception as e:
            if GlobalManager().debug:
                print(traceback.format_exc())
                print(e)

            if self.params.get('turn_on', True):
                GlobalManager().loop_turn_off()
            ForManager().destroy_for_stack()

    def end(self):
        if GlobalManager().debug:
            print(self.__stack)
        if self.params.get('key', None):
            GlobalManager().set(self.params['key'], copy.deepcopy(self.__stack))
        ForManager().set_depth()
        GlobalManager().loop_turn_on()
