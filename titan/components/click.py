# -*- coding: utf-8 -*-
from titan.components import Base
import time


class Click(Base):
    def default(self):
        self.driver.find_element_by_xpath(self.params['xpath']).click()
        self.sleep()
