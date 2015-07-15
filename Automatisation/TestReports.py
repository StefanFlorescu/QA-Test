__author__ = 'StefanFlorescu'

from Automatisation.ReportsPage import StatReports
import unittest


class ReportTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Reports(self):
        reports = StatReports()
        reports.go()
        reports.mg_login()

        reports.test_ReferenceDirectory()
        reports.test_CSVreport()
        reports.test_OverallTAT()
        reports.test_LandlordReport()
        reports.test_ActiveTasks()
        reports.test_ReferenceVolumes()
        reports.test_ReferenceDecisions()
        reports.test_RefereeResponse()
        reports.test_IncomingCommunications()
        reports.test_EquifaxDataSearch()
        reports.test_TenantsAccepts()
        reports.test_TenantProfile()
        reports.test_UserActivity()
        reports.test_ReferenceTurnaround()
        reports.test_TATbyReference()
        reports.test_ActiveApplicants()
        reports.test_ActionsReport()
        reports.test_LeadGeneration()

        # reports.close()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
