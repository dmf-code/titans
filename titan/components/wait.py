# -*- coding: utf-8 -*-
from titan.components import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Wait(Base):

    def have_element(self):
        WebDriverWait(self.driver, self.params.get('time', 10)).until(
            EC.presence_of_element_located(By.XPATH, self.params.get('xpath'))
        )

