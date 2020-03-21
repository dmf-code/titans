# -*- coding: utf-8 -*-
from titan.manages.global_manager import GlobalManager
from titan.utils.log import logger
from titan.hooks.base import Base
from titan import YAML_CONFIG
import traceback
from titan.utils import make_requests
import json
from titan import dirs


class Common(Base):

    def before(self, *args, **kwargs):
        pass

    def running(self, *args, **kwargs):
        pass

    def handle_data(self, *args, **kwargs):
        print(args)
        pass

    def after(self, *args, **kwargs):
        GlobalManager().get_driver().close()
        GlobalManager().get_driver().quit()

    def exception(self, *args, **kwargs):

        msg = 'exception: {} {}'.format(GlobalManager().get('commands.uuid'), traceback.format_exc())
        if GlobalManager().debug:
            print(msg)
        else:
            logger.error(msg)

    def terminate(self, *args, **kwargs):
        pass

    def get_args(self):
        return None

    def load_commands(self, *args, **kwargs):

        if YAML_CONFIG['load_command_from_file']:
            with open(dirs['configs'] + 'common.json', 'r', encoding='utf-8') as f:
                commands = json.load(f)
        else:
            res = make_requests('GET', 'http://localhost:5000/api/search/common/boss')
            commands = res['data']['jsonText']

        if isinstance(commands, str):
            commands = json.loads(commands)

        return commands
