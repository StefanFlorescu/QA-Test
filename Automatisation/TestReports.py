__author__ = 'StefanFlorescu'

from selenium import webdriver
from Automatisation.ReportsPage import StatReports
import unittest


class ReportTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Reports(self):
        reports = StatReports()
        reports.go()
        reports.mg_login()
        reports.test_ActiveApplicants()
        reports.test_CSVreport()
        reports.test_EquifaxData()
        reports.close()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()