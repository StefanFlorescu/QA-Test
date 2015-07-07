__author__ = 'StefanFlorescu'

from selenium import webdriver
import unittest


class MI_reports(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/StefanFlorescu/PycharmProjects/HomespunAutomation/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://letrisks-acumen.com/"


    def test_AgetLogin(self):
        self.driver.get(self.base_url + "?request=restart")
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("testinginbox@yahoo.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name("loginbutton").click()
        self.assertIn(self.driver.title, "Notifications")

    def test_ManagerLogin(self):
        self.driver.get(self.base_url + "?request=restart")
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("lr_manager@letrisks-acumen.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("lr_manager")
        self.driver.find_element_by_name("loginbutton").click()
        self.assertIn(self.driver.title, "Acumen")

    def test_OperatorLogin(self):
        self.driver.get(self.base_url + "?request=restart")
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("lr_manager@letrisks-acumen.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("lr_manager")
        self.driver.find_element_by_name("loginbutton").click()
        self.assertIn(self.driver.title, "Acumen")

    def test_AreaManagerLogin(self):
        self.driver.get(self.base_url + "?request=restart")
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("testingsitesqa@yandex.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name("loginbutton").click()
        self.assertIn(self.driver.title, "Notifications")

    def test_BranchManagerLogin(self):
        self.driver.get(self.base_url + "?request=restart")
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("testingsitesqa@outlook.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name("loginbutton").click()
        self.assertIn(self.driver.title, "Notifications")

    def test_AdministratorLogin(self):
        self.driver.get(self.base_url + "?request=restart")
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("testingsitesqa@yahoo.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name("loginbutton").click()
        self.assertIn(self.driver.title, "Notifications")

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()

