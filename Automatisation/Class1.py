__author__ = 'StefanFlorescu'

import selenium.webdriver.firefox
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class AgentLogin(unittest.TestCase):

    @classmethod
    def GoTo(self):
        """ initiate the browser object """

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://homespun.pre-prod.net/"
        self.verificationErrors = []
        self.accept_next_alert = True

if __name__ == '__main__':
    unittest.main()