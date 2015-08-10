__author__ = 'StefanFlorescu'

from Automatisation.ApplicationPage import ApplicationPage
import unittest

class ReportTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Reports(self):
        create = ApplicationPage()

        create.go()
        create.ag_login()
        create.create_app()
        create.wait(4)
        create.set_branch()
        create.set_property()
        create.set_rental_details(2000, 12)
        for i in (1, 2):
            create.set_tenant("Mr", "Test1", "Draytus", "Comprehensive", "1000")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
