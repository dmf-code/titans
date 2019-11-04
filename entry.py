# -*- coding: utf-8 -*-
import uuid
import argparse
from titan.core.engine import Engine
from titan.manages.global_manager import GlobalManager


class Entry(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Run Spider')
        self.args = self.build_parser()
        self.uuid = uuid.uuid1().__str__()

    def bootstrap(self):
        pass

    def build_parser(self):
        self.parser.add_argument('--type', dest='spider_type', required=True, help='spider type')
        self.parser.add_argument('--name', dest='task_name', required=True, help='task name')
        return self.parser.parse_args()

    def set(self, key, value):
        if not hasattr(self, key):
            setattr(self, key, value)

    def run(self):
        try:
            Engine(self.args.spider_type, self.args.task_name, self.uuid).scheduler()
        except Exception as e:
            print(e)
            driver = GlobalManager().get_driver()
            if driver is not None:
                driver.close()
                driver.quit()


if __name__ == '__main__':
    Entry().run()
