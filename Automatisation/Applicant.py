__author__ = 'StefanFlorescu'

from Automatisation.raw_data import applicants_pool as mass
import random


class Applicant(object):
    def __init__(self, ccj_value=False, phone_value=False, report="Comprehensive", hasemail=True,
                 incomeverification=True, payinadvance=True):

        def user_index():
            """ func that returns the index of the object that meets the initializator variable values(requirements)
            :return: int
            """
            index = 0
            while True:
                index = random.randint(0, (mass.__len__() - 1))
                if mass[index]["ccj"] == ccj_value and mass[index]["phone"] == phone_value:
                    break
            return mass[index]

        self.selector = user_index()
        self.report_type = report
        self.payinginadvance = payinadvance
        self.hasemail = hasemail
        self.incomeverification_required = incomeverification
        self.rentshare = 1000

    def set_report_type(self, value):
        self.report_type = value

    @property
    def name(self):
        return self.selector["name"][0]

    @property
    def surename(self):
        return self.selector["name"][1]

    @property
    def birthdate(self):
        return self.selector["name"][2]

    @property
    def current_address(self):
        return self.selector["address"][0]

    @property
    def previous_address(self):
        return self.selector["address"][1]

    @property
    def second_previous_address(self):
        return self.selector["address"][2]

    @property
    def sort_code(self):
        return self.selector["bank"][0]

    @property
    def account_number(self):
        return self.selector['bank'][1]

    @property
    def applicant_title(self):
        return self.selector["details"][0]

    @property
    def sex(self):
        return self.selector["details"][1]

    @property
    def origin(self):
        return self.selector["details"][2]

    @property
    def status(self):
        return self.selector["details"][3]