# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from titan.components import Base


class Input(Base):

    def clear(self):
        element = self.driver.find_element_by_xpath(self.params['xpath'])
        if self.params.get('clear', None):
            element.clear()
            return True

        element.click()
        space_num = self.params['space']if self.params.get('space', None) else 4
        while space_num:
            space_num -= 1
            element.send_keys(Keys.BACK_SPACE)

    def text(self):
        print(self.params)
        element = self.driver.find_element_by_xpath(self.params['xpath'])
        element.send_keys(self.params['text'])

