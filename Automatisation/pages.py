__author__ = 'Steve'

from Automatisation.browser import Browser

class LoginPage(object):

    def Initiate(self):
        self.driver = Browser()

    def GoTo(self):
        Browser.GoTo()

    def AgLogin(self):
        """
the function that executes agent login procedure

        """
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("lr_manager@letrisks-acumen.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("lr_manager")
        self.driver.find_element_by_name("loginbutton").click()
        self.assertIn(self.driver.title, "Acumen")