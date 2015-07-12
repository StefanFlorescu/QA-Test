__author__ = 'Steve'

import abc


class BasePage(object):
    """ All page objects inherit from this"""

    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver


    @abc.abstractmethod
    def _validate_page(self, driver):
        return

""" Regions define functionality available throughall page objects"""

    @property
    def search(self):
        from search import SearchRegion

        return SearchRegion(self.driver)

