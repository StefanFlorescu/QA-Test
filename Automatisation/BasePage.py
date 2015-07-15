__author__ = 'StefanFlorescu'

import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
import time
import random



class BasePage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://letrisks-acumen.com'
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.start_month = 6
        self.end_month = 7
        self.startday = 16
        self.endday = 27

    def go(self):
        self.driver.get(self.base_url + '/?request=restart')

    def ag_login(self):
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("testinginbox@yahoo.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name("loginbutton").click()

    def mg_login(self):
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("lr_manager@letrisks-acumen.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("lr_manager")
        self.driver.find_element_by_name("loginbutton").click()

    def op_login(self):
        self.go()
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("testingsitesqa@hotmail.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name("loginbutton").click()

    def logout(self):
        self.driver.find_element_by_partial_link_text("Account").click()
        self.driver.find_element_by_link_text("Logout").click()

    def access_profile(self):
        self.driver.find_element_by_partial_link_text("Account").click()
        self.driver.find_element_by_link_text("Profile").click()

    def create_app(self):
        self.driver.find_element_by_partial_link_text("Tenancy Application").click()
        self.driver.find_element_by_link_text("Create Application").click()

    def list_apps(self):
        self.driver.find_element_by_partial_link_text("Tenancy Application").click()
        self.driver.find_element_by_link_text("List Applications").click()

    def filter_byaddress(self, tenancy_address):
        self.list_apps()
        filter = self.driver
        filter.find_element_by_name("filter[address]").send_keys(tenancy_address + Keys.ENTER)

    def random_address(self, postcode):
        address = self.driver
        address.find_element_by_name("PostCode").clear()
        address.find_element_by_name("PostCode").send_keys(postcode + Keys.TAB + Keys.ENTER)
        address_list = address.find_elements_by_class_name("address_item")
        return type(address_list)

    def set_startdate(self):
        self.driver.find_element_by_name('sdate').click()
        picker = self.driver.find_element_by_id("ui-datepicker-div")
        select = Select(picker.find_element_by_class_name('ui-datepicker-month'))
        select.select_by_index(self.start_month)
        picker.find_element_by_link_text(str(self.startday)).click()

    def set_enddate(self):
        self.driver.find_element_by_name("edate").click()
        picker = self.driver.find_element_by_id("ui-datepicker-div")
        picker.find_element_by_link_text(str(self.endday)).click()

    def set_date(self):
        self.driver.find_element_by_name("date").click()
        datepicker = self.driver.find_element_by_id("ui-datepicker-div")
        datepicker.find_element_by_link_text(str(self.startday)).click()

    def close(self):
        self.driver.close()

    @property
    def title(self):
        return self.driver.title

    @property
    def webdriver(self):
        return self.driver

    @staticmethod
    def wait(period=2):
        time.sleep(period)

    def set_randomoption(self, name_attribute):
        driver = self.driver
        options = driver.find_element_by_name(str(name_attribute))
        select = Select(driver.find_element_by_name(str(name_attribute)))
        select.select_by_index(
            random.randint(1, len(options.find_elements_by_tag_name("option"))))

    def select_all(self, name_attribute):
        driver = self.driver
        elem = driver.find_element_by_name(str(name_attribute))
        options = elem.find_elements_by_tag_name("option")
        for option in options:
            option.click()

    def trigger_filter(self):
        self.driver.find_element_by_xpath('//input[@value="Filter"]').click()