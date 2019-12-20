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
        if GlobalManager().component_type == 'start':
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
            print(element.text)

        if self.params.get('tag_name', None):
            element = element.find_element_by_tag_name(self.params['tag_name'])

        self.__stack[self.params['key']] = screening_value(element, self.params)

    def start(self):
        try:
            ForManager().for_loop_start()
        except Exception as e:
            print(traceback.format_exc())
            if self.params.get('turn_on', True):
                GlobalManager().loop_turn_off()
            ForManager().destroy_for_stack()
            print(e)

    def end(self):
        print(self.__stack)
        if self.params.get('key', None):
            GlobalManager().set(self.params['key'], copy.deepcopy(self.__stack))
        # print(GlobalManager().get('job_list_custom_array'))
        ForManager().set_depth()
        GlobalManager().loop_turn_on()
