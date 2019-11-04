# -*- coding: utf-8 -*-
from inspect import isfunction
import requests
import json
import os


def convert_big_hump(string, space_character='_'):
    string_list = string.split(space_character)
    hump_string = ''
    for word in string_list:
        hump_string += word.capitalize()

    return hump_string


def make_requests(method, url, **kwargs):
    closure = None
    if kwargs.get('closure', None):
        closure = kwargs.pop('closure')
    result = requests.request(method, url, **kwargs, timeout=60)
    if 200 <= result.status_code < 300:
        if isfunction(closure):
            closure(result)
        if result.headers.get('Content-Type', None) == 'application/json':
            res = json.loads(result.text)
            return res
        return result.text
    content = 'method: {}, url: {}, args: {}{}'.format(method, url, kwargs, os.linesep)
    raise requests.HTTPError(content + result.reason)
