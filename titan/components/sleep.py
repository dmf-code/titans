# -*- coding: utf-8 -*-
from titan.components import Base
import time


class Sleep(Base):
    def default(self):
        if self.params.get('time', None):
            time.sleep(self.params['time'])
