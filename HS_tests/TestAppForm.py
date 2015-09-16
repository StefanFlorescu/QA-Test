__author__ = 'StefanFlorescu'

import unittest
from Automatisation.ApplicationForm import ApplicationForm
from Automatisation.Income import Income
from Automatisation.User import User

class ApplicationFormTest(unittest.TestCase):

    def setUp(self):
        global agent, main_income
        agent = User("testing", "Draytus", "agent")
        main_income = Income(1)

    def test_1_getapplication(self):
        application = ApplicationForm()
        application.login(agent)
        application.go(link = "/application/ShowUpdateApplicant/?apid=2257&agid=419&a_id=3890&open=2257")
        application.set_applicat_personal_details()
        application.set_maininc(main_income)
        application.set_addinc(1)
        application.set_address_history(["1-4 ", "100 ", "101 "])
        application.set_bank_details()
        application.set_nextofkin()
        application.set_additional_details()
