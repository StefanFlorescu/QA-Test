__author__ = 'StefanFlorescu'

import unittest

from Automatisation.ReportsPage import StatReports


class ReportTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_should_generate_all_MI_Reports(self):
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
        # reports.make_activeapplicantsreport()
        # reports.make_activeapplicationsreport()
        # reports.make_actionsreport()
        # reports.make_leadgenerationreport()
        reports.make_procstats()
        reports.make_refobtaining()
        reports.make_communstatsreport()
        reports.make_outstandingwork()
        reports.make_tenantappoutcome()
        reports.workitemreport()
        reports.close()

    def test_users_login(self):
        user = StatReports()
        user.ag_login()
        user.access_profile()
        user.logout()

        user.op_login()
        user.access_profile()
        user.logout()

        user.mg_login()
        user.access_profile()
        user.logout()

        user.admin_login()
        user.access_profile()
        user.logout()

        user.branch_login()
        user.access_profile()
        user.logout()

        user.area_login()
        user.access_profile()
        user.logout()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
