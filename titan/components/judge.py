# -*- coding: utf-8 -*-
from titan.components import Base
from titan.manages.global_manager import GlobalManager


class Judge(Base):

    def can_click_loop(self):
        element = self.driver.find_element_by_xpath(self.params['xpath'])
        if element.is_enabled():
            return GlobalManager().loop_turn_on()

        return GlobalManager().loop_turn_off()

    def default(self):
        pass
