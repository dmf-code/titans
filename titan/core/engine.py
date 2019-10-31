# -*- coding: utf-8 -*-
from titan.manages.factory_manager import FactoryManager
from titan.manages.global_manager import GlobalManager
from titan.manages.hook_manager import HookManager
from titan.core.browser import Chrome
import re
import os


class Engine(object):
    def __init__(self, spider_type, task_name, uuid):
        driver = Chrome().build()
        GlobalManager().build(spider_type, task_name, uuid)
        GlobalManager().set_driver(driver)
        self.hook = HookManager().build(spider_type)
        self.args = self.hook.get_args()
        self.commands = self.hook.load_commands()
        print(self.hook)

    def scheduler(self):
        self.hook.before()
        try:
            print(self.commands)
            self.execute(self.commands, 0)
        except Exception as e:
            self.hook.exception(e)
        finally:
            self.hook.after()

    def execute(self, commands, depth):
        for command in commands:
            if isinstance(command, list):
                return self.execute(command, depth + 1)
            component_name = command['component'].lower()
            component_args = command.get('args', {})

            print('if_status: ', GlobalManager().if_flag)
            print('break_status: ', GlobalManager().break_flag)
            if GlobalManager().break_flag:
                break

            if component_name != 'if' and GlobalManager().if_flag:
                continue

            if command.get('db_args', None):
                component_args['db_args'] = GlobalManager().get(component_args['dbArgs'], '_db_args')

            component = FactoryManager().build(component_name, component_args)

            type_ = command.get('type', 'default')

            print('command: ', command, depth)

            result = self.result_filter(component_args, component.run(type_))

            if command.get('return', None):
                GlobalManager().set(command['return'], result)

            print('loop_status: ', GlobalManager().loop_flag)

            if GlobalManager().loop_flag:
                self.execute(command, depth + 1)

            print(os.linesep)

    @staticmethod
    def result_filter(component_args, text):
        if component_args.get('filter', None) is None:
            return text

        pattern = component_args.get('pattern', None)
        if pattern:
            index = component_args.get('index', None)
            text = re.match(pattern, text).group(index if index else 0)

        return text


if __name__ == '__main__':
    Engine('common', 'click', 'c').scheduler()
