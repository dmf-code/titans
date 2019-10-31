# -*- coding: utf-8 -*-
import os
import logging
import datetime
import coloredlogs
from logging import config
from titan import LOGS_DIR
from titan.abstracts.singleton import Singleton

coloredlogs.install(level='DEBUG')

today = datetime.datetime.now().strftime("%Y%m%d")

log_path = os.path.join(LOGS_DIR, f'titan_{today}.log')


class Log(object, metaclass=Singleton):
    VERSION = 1.0
    FORMATTERS = {
        'default': {
            'format': u"%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': u"%(name)s[%(process)d] %(levelname)s %(message)s",
        },
    }
    HANDLERS = {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1024,
            'backupCount': 1,
            'filename': log_path,
            'level': 'DEBUG',
            'formatter': 'default',
            'encoding': 'utf-8',
        },
    }
    LOGGERS = {
        'default': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        }
    }
    DEFAULT_LOGGING = {}

    def __init__(self):
        self.DEFAULT_LOGGING = {
            'version': self.VERSION,
            'formatters': self.FORMATTERS,
            'handlers': self.HANDLERS,
            'loggers': self.LOGGERS
        }
        self.logger = self.build()

    def update_logger_level(self, name='default', level='DEBUG'):
        self.LOGGERS.get(name)['level'] = level
        self.logger = self.build(name)
        return True

    def update_handle_level(self, name='default', level='DEBUG'):
        self.HANDLERS.get(name)['level'] = level
        self.logger = self.build(name)
        return True

    def build(self, name='default'):
        config.dictConfig(self.DEFAULT_LOGGING)
        return logging.getLogger(name)


log = Log()
logger = log.build()

if __name__ == '__main__':
    logger.debug('123')
    log.update_logger_level(level='INFO')
    logger.info('4444')
