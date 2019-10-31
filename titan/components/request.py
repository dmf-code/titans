# -*- coding: utf-8 -*-
from titan.manages.global_manager import GlobalManager
from titan.utils import make_requests
from titan.components import Base
import time


class Request(Base):
    def url_format(self):
        if self.params.get('url', None):
            global_type = self.params.get('global_type', None)
            print('global_type：', global_type)
            if global_type is None:
                params = GlobalManager().get()
            else:
                params = GlobalManager().get(type_=global_type)
            url = self.params['url'].format(**params)
            return url

    def get_method(self):
        return self.params.get('method', 'POST')

    def browser(self):
        url = self.url_format()
        self.driver.get(url)
        return self.sleep()

    def default(self):
        url = self.url_format()
        data = self.params.get('data', [])
        make_requests(self.get_method(), url, data=data)
