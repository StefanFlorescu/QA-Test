__author__ = 'StefanFlorescu'

import unittest
from Automatisation.ApplicationForm import ApplicationForm

class ApplicationFormTest(unittest.TestCase):

    def test_1_getapplication(self):
        appplication = ApplicationForm()
        appplication.mg_login()
        appplication.go(link = "//application/ShowUpdateApplicant/?apid=555&agid=1421&a_id=1437&open=555")
        appplication.set_applicat_personal_details()
        appplication.set_maininc()
        appplication.set_addinc(1)
        appplication.set_address_history(["1-4 ", "100 ", "101 "])
        appplication.set_bank_details()
        appplication.set_nextofkin()
        appplication.set_additional_details()
