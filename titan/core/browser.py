# -*- coding: utf-8 -*-
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from titan.manages.global_manager import GlobalManager
from fake_useragent import UserAgent
from selenium import webdriver
from titan import dirs, YAML_CONFIG
import random


class Chrome(object):
    def __init__(self):
        self.driver = self.set_chrome()

    @staticmethod
    def enable_download_in_headless_chrome(driver, download_dir):
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/' + driver.session_id + '/chromium/send_command'
        )
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        command_result = driver.execute("send_command", params)
        if GlobalManager().debug:
            print(command_result)

    def set_chrome(self):

        prefs = {
            "download": {
                "default_directory": dirs['storages'],
                "prompt_for_download": False,
                "directory_upgrade": True
            }
        }

        chrome_options = Options()

        if YAML_CONFIG['headless']:
            chrome_options.add_argument('--headless')
            self.enable_download_in_headless_chrome(self.driver, dirs['storages'])

        for arg in YAML_CONFIG['browser_args']:
            chrome_options.add_argument(arg)
        chrome_options.add_argument('user-agent={}'.format(UserAgent().random))

        for k, v in YAML_CONFIG['experimental_option'].items():
            if k == 'prefs':
                chrome_options.add_experimental_option('prefs', {**prefs, **v})
            else:
                chrome_options.add_experimental_option(k, v)

        d = DesiredCapabilities.CHROME
        if YAML_CONFIG.get("hub", None) is None:
            print(chrome_options)
            chromedriver_path = dirs['bin'] + 'chromedriver.exe'
            chrome = webdriver.Chrome(chromedriver_path, chrome_options=chrome_options, desired_capabilities=d)
        else:
            hub = YAML_CONFIG['hub'][random.randint(0, len(YAML_CONFIG['hub']) - 1)]
            chrome = webdriver.Remote(command_executor=hub, desired_capabilities=d)

        return chrome

    def build(self):
        return self.driver
