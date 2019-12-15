# -*- coding: utf-8 -*-
from titan.components import Base


class Window(Base):

    def before(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def after(self):
        self.driver.switch_to_window(self.driver.window_handles[0])
