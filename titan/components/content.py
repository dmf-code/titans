# -*- coding: utf-8 -*-
from titan.components import Base
import re


class Content(Base):

    def default(self):
        if not self.driver.find_elements_by_xpath(self.params['xpath']):
            if self.params.get('default', None) is not None:
                return self.params['default']

        element = self.driver.find_element_by_xpath(self.params['xpath'])
        attr = self.params.get('attr', None)
        text = element.get_attribute(attr) if attr else element.text

        return text
