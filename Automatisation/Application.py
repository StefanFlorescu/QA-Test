__author__ = 'StefanFlorescu'

class Application (object):

    def __init__(self):
        self.rental_amount = 2000
        self.tenancy_term = 12
        self.tenancy_start = "31/08/2015"
        self.tency_adddress = ""

    def set_tenacy_address(self, new):
        self.tency_adddress.__add__(new)


    # def landlord_details(self):