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
        self.address_district = ""
        self.address_town = ""
        self.address_county = ""



    def set_adress(self, postcode, house_number, house_name, flat, street, district, town, county):
        self.address_postcode = postcode
        self.address_house_name = house_name
        self.address_house_nr = house_number
        self.address_flat = flat
        self.address_street = street
        self.address_district = district
        self.address_town = town
        self.address_county = county

    def set_tenancy_address(self, full_address):
        self.tency_adddress = full_address



    # def landlord_details(self):