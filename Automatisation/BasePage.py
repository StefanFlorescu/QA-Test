__author__ = 'StefanFlorescu'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import random


class BasePage(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://homespun.lan'
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.year = 2015
        self.start_month = 7
        self.end_month = 7
        self.startday = 4
        self.endday = 30
        if self.base_url.__contains__("letrisks-acumen"):
            self.postcode = "IV44 8TZ"
        else:
            self.postcode = "BA133BN"


    def go(self, link='/?request=restart'):
        self.driver.get(self.base_url + link)

    def login(self, user="testinginbox@yahoo.com", password=123456):
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys(user)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(str(password))
        self.driver.find_element_by_name("loginbutton").click()

    def ag_login(self):
        self.go()
        self.login()

    def mg_login(self):
        self.go()
        self.login("lr_manager@letrisks-acumen.com", "lr_manager")

    def op_login(self):
        self.go()
        self.login("testingsitesqa@hotmail.com", 123456)

    def admin_login(self):
        self.go()
        self.login("testingsitesqa@yahoo.com", 123456)

    def branch_login(self):
        self.go()
        self.login("testingsitesqa@outlook.com", 123456)

    def area_login(self):
        self.go()
        self.login("testingsitesqa@yandex.com", 123456)

    def logout(self):
        self.driver.find_element_by_partial_link_text("Account").click()
        self.driver.find_element_by_link_text("Logout").click()



    def click_button_byname(self, name_attribute="build"):
        driver = self.driver
        driver.find_element_by_name(name_attribute).click()

    def click_button_byvalue(self, value="Submit"):
        driver = self.driver
        driver.find_element_by_xpath('//input[@value=\"{0}\"]'.format(str(value))).click()

    def click_button_byid(self, id_attribute="build"):
        driver = self.driver
        driver.find_element_by_id(id_attribute).click()

    def click_button_byxath(self, attribute="build"):
        driver = self.driver
        driver.find_element_by_xpath(attribute).click()



    def goto_menuoption(self, menu = "MI", partial_text="Reference directory"):
        driver = self.driver
        driver.find_element_by_partial_link_text(menu).click()
        self.wait()
        driver.find_element_by_partial_link_text(partial_text).click()

    def access_profile(self):
        self.goto_menuoption("Account", "Profile")

    def list_apps(self):
        self.goto_menuoption("Tenancy Application", "List Applications")

    def list_dashboard(self):
        self.driver.find_element_by_partial_link_text("Home").click()
        self.wait()

    def filter_byaddress(self, tenancy_address):
        self.list_apps()
        filter = self.driver
        filter.find_element_by_name("filter[address]").send_keys(tenancy_address + Keys.ENTER)



    def set_randomaddress(self, postcode):
        address = self.driver
        address.find_element_by_name("PostCode").clear()
        address.find_element_by_name("PostCode").send_keys(postcode + Keys.TAB + Keys.ENTER)
        address_list = address.find_elements_by_class_name("address_item")
        address_list[random.randint(0, address_list.__len__() - 1)].click()

    def set_singledate(self):
        self.set_date("date", self.start_month, self.year, self.startday)

    def set_startdate(self, locator="sdate"):
        self.set_date(locator, self.start_month, self.year, self.startday)

    def set_enddate(self, locator="edate"):
        self.set_date(locator, self.end_month, self.year, self.endday)

    def set_date(self, locator_name, month, year, day):
        self.driver.find_element_by_name(locator_name).click()
        self.wait(0)
        self.select_optionbyxpath(
            '//div[@class="ui-datepicker-title"]/select[@class="ui-datepicker-month"]', month)
        self.select_optionbyxpath(
            '//div[@class="ui-datepicker-title"]/select[@class="ui-datepicker-year"]', year)
        datepicker = self.driver.find_element_by_id("ui-datepicker-div")
        datepicker.find_element_by_link_text(str(day)).click()



    def select_randomoption_byname(self, name_attribute):
        driver = self.driver
        options = driver.find_element_by_name(str(name_attribute))
        select = Select(options)
        select.select_by_index(
            random.randint(1, len(options.find_elements_by_tag_name("option")) - 1))

    def select_randomoption_byxpath(self, attribute):
        driver = self.driver
        options = driver.find_element_by_xpath(str(attribute))
        select = Select(options)
        select.select_by_index(
            random.randint(1, len(options.find_elements_by_tag_name("option")) - 1))

    def select_all_byname(self, name_attribute):
        driver = self.driver
        elem = driver.find_element_by_name(str(name_attribute))
        options = elem.find_elements_by_tag_name("option")
        for option in options:
            option.click()

    def select_all_byxpath(self, select_id):
        driver = self.driver
        elem = driver.find_element_by_xpath(select_id)
        options = elem.find_elements_by_tag_name("option")
        for option in options:
            option.click()

    def select_option_byname(self, select_id, select_option):
        driver = self.driver
        Select(driver.find_element_by_name(select_id)).select_by_visible_text(select_option)

    def select_option_byid(self, select_id, select_option):
        driver = self.driver
        Select(driver.find_element_by_id(select_id)).select_by_visible_text(select_option)

    def select_optionbyxpath(self, select_id, select_option):
        driver = self.driver
        if type(select_option) == str:
            Select(driver.find_element_by_xpath(select_id)).select_by_visible_text(select_option)
        if type(select_option) == int:
            Select(driver.find_element_by_xpath(select_id)).select_by_value(str(select_option))



    def get_element_byngmodel(self, model):
        driver = self.driver
        return driver.find_element_by_xpath('//input[@ng-model=\"{0}\"]'.format(str(model)))

    def close(self):
        self.driver.close()

    @property
    def title(self):
        return self.driver.title

    @property
    def webdriver(self):
        return self.driver

    @staticmethod
    def wait(period=1):
        time.sleep(period)
