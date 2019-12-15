# -*- coding: utf-8 -*-
from abc import abstractmethod
from titan.abstracts.singleton import Singleton


class Base(metaclass=Singleton):
    @abstractmethod
    def before(self, *args, **kwargs):
        pass

    @abstractmethod
    def running(self, *args, **kwargs):
        pass

    @abstractmethod
    def handle_data(self, *args, **kwargs):
        pass

    @abstractmethod
    def after(self, *args, **kwargs):
        pass

    @abstractmethod
    def exception(self, *args, **kwargs):
        pass

    @abstractmethod
    def terminate(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_args(self):
        pass

    @abstractmethod
    def load_commands(self, *args, **kwargs):
        pass
