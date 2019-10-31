# -*- coding: utf-8 -*-
from titan.manages.global_manager import GlobalManager
from titan.components import Base


class If(Base):

    def start_block(self):
        GlobalManager().if_turn_off()
        if self.params.get('xpath', None) and self.driver.find_elements_by_xpath('xpath'):
            GlobalManager().if_turn_on()
            return True

        if self.params.get('not_exist_xpath', None) and not self.driver.find_elements_by_xpath('not_exist_xpath'):
            GlobalManager().if_turn_on()
            return True

        if self.params.get('attr_xpath', None) and self.driver.find_element_by_xpath('attr_xpath')\
                .get_attribute(self.params['attr']):
            GlobalManager().if_turn_on()
            return True

        return False

    @staticmethod
    def end_block():
        GlobalManager().if_turn_off()

    def default(self):
        pass
