

__author__ = 'StefanFlorescu'

from Automatisation.ApplicationPage import ApplicationPage
from Automatisation import applicants
from Automatisation import users
from Automatisation.Application import Application
import unittest

user = users.User(instance="homespun")
application = Application()
applicant_list = [applicants.Applicant() for i in range(3)]


class ApplicationGroupTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_create_application(self):
        create = ApplicationPage()
        create.ag_login()
        create.create_app()
        create.set_branch(user.branch)
        create.set_property()
        application.set_adress(create.postcode, create.get_housenumber, create.get_housename, create.get_flat,
                               create.get_street, create.get_district, create.get_town, create.get_county)
        create.set_rental_details(2000, 12)
        tenant = applicant_list[0]
        create.set_tenant(tenant.title, tenant.name, tenant.surename, tenant.report_type, tenant.rentshare, 1)
        tenant = applicant_list[1]
        create.set_tenant(tenant.title, tenant.name, tenant.surename, "Instant", tenant.rentshare, 2)
        guarantor = applicant_list[2]
        create.set_guarantor(guarantor.title, guarantor.name, guarantor.surename, guarantor.report_type)
        create.click_button_byvalue()
        create.wait(10)
        self.assertIn(create.driver.title, "Complete application", "Error creating application !")
        create.list_dashboard()


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
