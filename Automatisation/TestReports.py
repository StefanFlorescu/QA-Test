__author__ = 'StefanFlorescu'

import unittest

from Automatisation.ReportsPage import StatReports


class ReportTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Reports(self):
        reports = StatReports()
        reports.mg_login()

        # reports.make_referencedirectory()
        # reports.make_csvreport()
        # reports.make_overalltat()
        # reports.make_landlordreport()
        # reports.make_activetasksreport()
        # reports.make_referencevolreport()
        # reports.make_refdecisionreport()
        # reports.make_refresponsereport()
        # reports.make_incomcommreport()
        # reports.make_equifaxdatasearchreport()
        # reports.make_tenantacceptsreport()
        # reports.make_tenantprofilereport()
        # reports.make_useractivityreport()
        # reports.make_refturnaroundreport()
        # reports.make_tatbyrefreport()
        reports.make_activeapplicantsreport()
        reports.make_activeapplicationsreport()
        reports.make_actionsreport()
        reports.make_leadgenerationreport()
        reports.close()

    # def test_user_login(self):
    #     users = StatReports()
    #     users.ag_login()
    #     users.op_login()
    #     users.mg_login()
    #     users.admin_login()
    #     users.branch_login()
    #     users.area_login()
    #     users.close()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
