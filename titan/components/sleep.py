# -*- coding: utf-8 -*-
from titan.components import Base
import random
import time


class Sleep(Base):
    def random(self):
        start = self.params.get('start', 5)
        end = self.params.get('end', 8)
        step = self.params.get('step', 1)
        time.sleep(random.randrange(start, end, step))

    def default(self):
        if self.params.get('time', None):
            time.sleep(self.params['time'])
