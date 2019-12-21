# -*- coding: utf-8 -*-
from titan.manages.container_manager import ContainerManager
from titan.manages.global_manager import GlobalManager
from titan.manages.hook_manager import HookManager
from titan.core.browser import Chrome
from titan.utils import make_requests
from titan import YAML_CONFIG, dirs
import re


class Engine(object):
    def __init__(self, spider_type, task_name, uuid, debug):
        driver = Chrome().build()
        GlobalManager().build(spider_type, task_name, uuid)
        GlobalManager().set_driver(driver)
        self.hook = HookManager().build(spider_type)
        self.args = self.hook.get_args()
        self.commands = self.hook.load_commands()
        if debug:
            GlobalManager().debug = debug
        if GlobalManager().debug:
            print(self.hook)

    def scheduler(self):
        self.hook.before()
        try:
            if GlobalManager().debug:
                print(self.commands)
            self.execute(self.commands, 0)
            self.handle_data()
        except Exception as e:
            self.hook.exception(e)
        finally:
            self.hook.after()

    def execute(self, commands, depth):
        GlobalManager().if_turn_on()
        GlobalManager().depth = depth
        for command in commands:

            if isinstance(command, list):
                self.execute(command, depth + 1)
                GlobalManager().if_turn_on()

                while GlobalManager().is_loop:
                    self.execute(command, depth + 1)
                    GlobalManager().if_turn_on()

                GlobalManager().depth = depth
                continue

            component_name = command['component'].lower()
            component_args = command.get('args', {})
            component_type = command.get('type', 'default')

            if GlobalManager().debug:
                print('#--------------------------------------#')
                print('exec command: ', command)
                print('before_if_status: ', GlobalManager().is_if)
                print('before_break_status: ', GlobalManager().is_break)
                print('before_loop_status: ', GlobalManager().is_loop)

            if command.get('db_args', None):
                component_args['db_args'] = GlobalManager().get(component_args['dbArgs'], '_db_args')

            GlobalManager().component_name = component_name
            GlobalManager().component_type = component_type

            component = ContainerManager().build(component_name, component_args)

            result = self.result_filter(component_args, component.run(component_type))

            if command.get('return', None):
                GlobalManager().set(command['return'], result)
            if GlobalManager().debug:
                print('after_if_status: ', GlobalManager().is_if)
                print('after_break_status: ', GlobalManager().is_break)
                print('after_loop_status: ', GlobalManager().is_loop)

            if component_name == 'if' and not GlobalManager().is_if:
                return

            if GlobalManager().is_break:
                return

            if not GlobalManager().is_loop:
                return

    def handle_data(self):
        data = GlobalManager().get()
        storage_type = YAML_CONFIG['callback']['default']
        callback = YAML_CONFIG['callback']['stores']
        if storage_type == 'file':
            self.hook.handle_data(data)
        elif storage_type == 'request':
            task_json = {
                'type': GlobalManager().get('spider_type', '_system'),
                'name': GlobalManager().get('task_name', '_system'),
                'uuid': GlobalManager().get('uuid', '_system'),
                'result': data
            }
            res = make_requests('POST', callback['request']['url'], json=task_json)
            if GlobalManager().debug:
                print(res)

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
