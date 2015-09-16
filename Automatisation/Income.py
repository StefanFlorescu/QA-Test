__author__ = 'StefanFlorescu'
from Automatisation.raw_data import income_pool


class Income(object):

    def __init__(self, income_number):
        self.income = income_pool[income_number]

    @property
    def get_type(self):
        return self.income["type"]

    @property
    def name(self):
        return self.income["name"]

    @property
    def data(self):
        return self.income["data"]
