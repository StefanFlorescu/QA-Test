__author__ = 'StefanFlorescu'
import random

class Application (object):

    def __init__(self):
        self.rental_amount = 2000
        self.tenancy_term = 12
        self.tenancy_start = "31/08/2015"
        self.tency_adddress = ""
        self.address_postcode = "BA133bn"
        self.address_house_nr = ""
        self.address_flat = ""
        self.address_house_name = ""
        self.address_street = ""
        self.address_disctrict = ""
        self.address_town = ""
        self.address_county = ""



    def set_tenacy_address(self, new):
        self.tency_adddress.__add__(new)


    # def landlord_details(self):