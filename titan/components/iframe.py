# -*- coding: utf-8 -*-
from titan.components import Base


class Iframe(Base):

    def default(self):
        if self.params.get('frame_id', None):
            return self.driver.switch_to.frame(self.params['frame_id'])

        if self.params.get('xpath', None):
            return self.driver.switch_to.frame(
                self.driver.find_element_by_xpath(self.params['xpath'])
            )
