# -*- coding: utf-8 -*-
from titan.components import Base
from titan.manages.global_manager import GlobalManager


class While(Base):
    def start(self):
        pass

    def end(self):
        if self.params.get('xpath', None):
            if not self.driver.find_elements_by_xpath(self.params['xpath']):
                return GlobalManager().loop_turn_on()

        if self.params.get('key', None):
            if GlobalManager.get(self.params['key'], '_db_args'):
                return GlobalManager().loop_turn_on()

        return GlobalManager().loop_turn_off()
