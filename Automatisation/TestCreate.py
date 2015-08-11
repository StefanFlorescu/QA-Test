__author__ = 'StefanFlorescu'

from Automatisation.ApplicationPage import ApplicationPage
from Automatisation import applicants
from Automatisation import users
import unittest

user = users.User()
tenant_list = [applicants.Applicant() for i in range(2)]


class ReportTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_Reports(self):
        create = ApplicationPage()
        create.go()
        create.ag_login()
        create.create_app()
        create.wait(3)
        create.set_branch("LetRisks")
        create.set_property()
        create.set_rental_details(2000, 12)
        tenant_order =1
        for tenant in tenant_list:
            create.set_tenant(tenant.title, tenant.name, tenant.surename, tenant.report_type, tenant.rentshare,
                              tenant_order)
            tenant_order = 1+ tenant_order
        #create.set_guarantor()


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
