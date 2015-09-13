__author__ = 'StefanFlorescu'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.by import By
import time
import random


class BasePage(object):
    def __init__(self, instance_url= 'http://sandbox.letrisks-acumen.com'):
        self.driver = webdriver.Firefox()
        self.base_url = instance_url
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.start_date = "01/08/2015"
        self.end_date = time.strftime("%d/%m/%Y")
        if self.base_url.__contains__("letrisks-acumen"):
            self.postcode = "IV44 8TZ"
        else:
            self.postcode = "BA133BN"



    def go(self, link='/?request=restart'):
        self.driver.get(self.base_url + link)

    def login(self, user_object):
        self.go()
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys(user_object.username)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(str(user_object.password))
        self.driver.find_element_by_name("loginbutton").click()

    def logout(self):
        self.driver.find_element_by_partial_link_text("Account").click()
        self.driver.find_element_by_link_text("Logout").click()



    def click_button_byname(self,  name_attribute="build"):
        driver = self.driver
        driver.find_element_by_name(name_attribute).click()

    def click_button_byvalue(self, value="Submit"):
        driver = self.driver
        driver.find_element_by_xpath('//input[@value=\"{0}\"]'.format(str(value))).click()

    def click_button_byid(self, id_attribute="build"):
        driver = self.driver
        driver.find_element_by_id(id_attribute).click()

    def click_button_byxath(self, attribute="build", value="True"):
        driver = self.driver
        driver.find_element_by_xpath('//input[@\"{0}\"=\"{1}\"]'.format(str(attribute), str(value))).click()



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



    def set_randomaddress(self, postcode_name="PostCode"):
        address = self.driver.find_element_by_xpath("//input[contains(@name,\"{}\")]".format(postcode_name))
        address.clear()
        address.send_keys(self.postcode + Keys.TAB + Keys.ENTER)
        address_list = self.driver.find_elements_by_class_name("address_item")
        address_list[random.randint(0, address_list.__len__() - 1)].click()

    def set_address(self, postcode_field_name, address_string):
        address = self.driver
        address.find_element_by_name(postcode_field_name).send_keys(self.postcode + Keys.TAB + Keys.ENTER)
        address.find_element_by_xpath('//li[@class="address_item" and contains(text(), \"{0}\")]'.format(str(address_string))).click()



    def set_singledate(self, webelement):
        self.set_date(webelement, "date", self.start_date)

    def set_startdate(self, webelement, locator="sdate"):
        self.set_date(webelement, locator, self.start_date)

    def set_enddate(self, webelement, locator="edate"):
        self.set_date(webelement, locator, self.end_date)

    def set_date(self, webelement, locator_name, date_string):
        webelement.find_element_by_xpath('//input[contains(@name,\"{0}\")]'.format(locator_name)).click()
        date_pool = date_string.split("/")
        day = self.format_date(date_pool[0])
        month = self.format_date(date_pool[1])
        year = self.format_date(date_pool[2])
        self.select_option_byxpath(webelement,
            '//div[@id="ui-datepicker-div"]/descendant::select[@class="ui-datepicker-month"]', int(month)-1)
        self.select_option_byxpath(webelement,
            '//div[@id="ui-datepicker-div"]/descendant::select[@class="ui-datepicker-year"]', year)
        datepicker = webelement.find_element_by_xpath('//table[@class="ui-datepicker-calendar"]/tbody')
        datepicker.find_element_by_link_text(str(day)).click()



    def input_date_byname(self, webelement, name_attribute, string_input):
        input = webelement.find_element_by_name(name_attribute)
        input.send_keys(string_input)



    def select_randomoption_byname(self, webelement, name_attribute):
        options = webelement.find_element_by_name(str(name_attribute))
        select = Select(options)
        select.select_by_index(
            random.randint(1, len(options.find_elements_by_tag_name("option")) - 1))

    def select_randomoption_byxpath(self, webelement, attribute):
        options = webelement.find_element_by_xpath(str(attribute))
        select = Select(options)
        select.select_by_index(
            random.randint(1, len(options.find_elements_by_tag_name("option")) - 1))

    def select_all_byname(self, webelement, name_attribute):
        elem = webelement.find_element_by_name(str(name_attribute))
        options = elem.find_elements_by_tag_name("option")
        for option in options:
            option.click()

    def select_all_byxpath(self, webelement, select_id):
        elem = webelement.find_element_by_xpath(select_id)
        options = elem.find_elements_by_tag_name("option")
        for option in options:
            option.click()

    def select_option_byname(self, webelement, select_id, select_option):
        if type(select_option) == str:
            Select(webelement.find_element_by_name(select_id)).select_by_visible_text(str(select_option))
        if type(select_option) == int:
            Select(webelement.find_element_by_name(select_id)).select_by_value(str(select_option))

    def select_option_byid(self, webelement, select_id, select_option):
        if type(select_option) == str:
            Select(webelement.find_element_by_id(select_id)).select_by_visible_text(str(select_option))
        if type(select_option) == int:
            Select(webelement.find_element_by_id(select_id)).select_by_value(str(select_option))

    def select_option_byxpath(self, webelement, select_id, select_option):
        if type(select_option) == str:
            Select(webelement.find_element_by_xpath(select_id)).select_by_visible_text(str(select_option))
        if type(select_option) == int:
            Select(webelement.find_element_by_xpath(select_id)).select_by_value(str(select_option))



    def get_element_byngmodel(self, model):
        driver = self.driver
        return driver.find_element_by_xpath('//input[@ng-model=\"{0}\"]'.format(str(model)))

    def wait_element(self, wait_time = 10, xpath="//div"):
        return WebDriverWait(self.driver, wait_time).until(expect.presence_of_element_located((By.XPATH, xpath)))

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

    @staticmethod
    def random_int(start=0, end=10):
        return random.randint(start, end)

    @staticmethod
    def format_date(string):
        if string.startswith("0"):
            return string[1:]
        else:
            return string