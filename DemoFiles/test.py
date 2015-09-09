__author__ = 'StefanFlorescu'

import random


class MyClass(object):
    def dothis(self):
        self.rand_val = random.randint(1,20)

myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)

print(); print();



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.by import By
import time
import random

class BasePage(object):
    def __init__(self, instance_url= 'https://google.com'):
        self.driver = webdriver.Firefox()
        self.base_url = instance_url
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.start_date = "01/08/2015"
        self.end_date = time.strftime("%d/%m/%Y")
        if self.base_url.__contains__("letrisks-acumen"):
            self.postcode = "IV44 8TZ"
        else:
            self.postcode = "BA133BN"

    def go(self):
        self.driver.get(self.base_url)

    def webinstance(self):
        return self

class ImagePage(BasePage):

    def __init__(self, instance):
       self.driver = instance

    def clilc_images(self):
        self.driver.find_element_by_link_text("Images").click()