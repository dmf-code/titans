# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('.')))

if __name__ == '__main__':
    from admin import init

    init()
