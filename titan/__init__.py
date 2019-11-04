# -*- coding: utf-8 -*-
import yaml
import os

TITAN_ENV = os.environ.get('TITAN_ENV', 'development')

# creative dir
TITAN_DIR = os.path.dirname(os.path.realpath(__file__))

BIN_DIR = TITAN_DIR + os.path.sep + 'bin' + os.path.sep

LOGS_DIR = TITAN_DIR + os.path.sep + 'logs' + os.path.sep

COMPONENTS_DIR = TITAN_DIR + os.path.sep + 'components' + os.path.sep

CONFIGS_DIR = TITAN_DIR + os.path.sep + 'configs' + os.path.sep

HOOKS_DIR = TITAN_DIR + os.path.sep + 'hooks' + os.path.sep

STORAGES_DIR = TITAN_DIR + os.path.sep + 'storages' + os.path.sep

dirs = {
    'titan': TITAN_DIR,
    'bin': BIN_DIR,
    'storages': STORAGES_DIR,
    'logs': LOGS_DIR,
    'components': COMPONENTS_DIR,
    'configs': CONFIGS_DIR,
    'hooks': HOOKS_DIR
}


class Config(object):
    __yaml_config = None

    def __init__(self):
        with open(TITAN_DIR + os.path.sep + 'titan.yml') as f:
            self.__yaml_config = yaml.load(f.read(), Loader=yaml.FullLoader)[TITAN_ENV]

    def __getattr__(self, item):
        print(item)


# load config
with open(TITAN_DIR + os.path.sep + 'titan.yml', encoding='utf-8') as f:
    YAML_CONFIG = yaml.load(f.read(), Loader=yaml.FullLoader)[TITAN_ENV]

if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)

if __name__ == '__main__':
    print(YAML_CONFIG)
    print(LOGS_DIR)
