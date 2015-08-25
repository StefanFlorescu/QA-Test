__author__ = 'StefanFlorescu'

import unittest
from Automatisation.ApplicationForm import ApplicationForm

class ApplicationFormTest(unittest.TestCase):

    def test_1_getapplication(self):
        appplication = ApplicationForm()
        appplication.ag_login()
        appplication.go(link = "//application/ShowUpdateApplicant/?apid=555&agid=1421&a_id=1437&open=555")
        appplication.set_applicat_personal_details()
        appplication.set_maininc()
        appplication.set_addinc(4)
        appplication.set_address(["1-4","100","101"])
