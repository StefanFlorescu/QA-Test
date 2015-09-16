__author__ = 'StefanFlorescu'

import unittest
from Automatisation.ReportsPage import StatReports
from Automatisation.User import User


class ReportTests(unittest.TestCase):

    def setUp(self):
        global manager, agent, operator, area_manager, branch_manager
        manager = User("testing", "Draytus", "manager")
        agent = User("testing", "Draytus", "agent")
        operator = User("testing", "Draytus", "operator")
        area_manager = User("testing", "Draytus", "area_manager")
        branch_manager = User("testing", "Draytus", "branch_manager")


    def test_should_generate_all_MI_Reports(self):
        reports = StatReports()
        reports.login(manager)

        reports.make_referencedirectory()
        reports.make_csvreport()
        reports.make_overalltat()
        reports.make_landlordreport()
        reports.make_activetasksreport()
        reports.make_referencevolreport()
        reports.make_refdecisionreport()
        reports.make_refresponsereport()
        reports.make_incomcommreport()
        reports.make_equifaxdatasearchreport()
        reports.make_tenantacceptsreport()
        reports.make_tenantprofilereport()
        reports.make_useractivityreport()
        reports.make_refturnaroundreport()
        reports.make_tatbyrefreport()
        reports.make_activeapplicantsreport()
        reports.make_activeapplicationsreport()
        reports.make_actionsreport()
        reports.make_leadgenerationreport()
        reports.make_procstats()
        reports.make_refobtaining()
        reports.make_communstatsreport()
        reports.make_outstandingwork()
        reports.make_tenantappoutcome()
        reports.workitemreport()
        reports.close()

    def test_users_login(self):
        user = StatReports()
        user.login(manager)
        user.access_profile()
        user.logout()

        user.login(agent)
        user.access_profile()
        user.logout()

        user.login(operator)
        user.access_profile()
        user.logout()

        user.login(area_manager)
        user.access_profile()
        user.logout()

        user.login(branch_manager)
        user.access_profile()
        user.logout()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
