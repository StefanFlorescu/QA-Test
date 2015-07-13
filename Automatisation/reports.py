__author__ = 'StefanFlorescu'

from selenium import webdriver
import unittest


class MI_reports(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/StefanFlorescu/PycharmProjects/HomespunAutomation/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://letrisks-acumen.com/"
        self.driver.get(self.base_url + "?request=restart")
        self.driver.find_element_by_id("text-password").clear()
        self.driver.find_element_by_id("text-password").send_keys("lr_manager@letrisks-acumen.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("lr_manager")
        self.driver.find_element_by_name("loginbutton").click()
        self.assertIn(self.driver.title, "Acumen")

    def test_CSVreport(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("CSV").click()
        self.assertIn("CSV Report", driver.title)
        driver.find_element_by_name("date").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_OverallTAT(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("TAT").click()
        self.assertIn("TAT", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_LandlordReport(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("The Landlord").click()
        self.assertIn("Landlord", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_ReferenceVolumes(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Reference Volumes").click()
        self.assertIn("Reference Volumes", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_ReferenceDecisions(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Reference Decisions").click()
        self.assertIn("Reference Decisions", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_RefereeResponse(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Referee Response").click()
        self.assertIn("Referee Response", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_IncomingCommunications(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Incoming Communications").click()
        self.assertIn("Incoming Communications", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_EquifaxData(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Equifax data").click()
        self.assertIn("Equifax Data Request", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_UserActivity(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("User Activity Report").click()
        self.assertIn("User Activity Report", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_TATbyReference(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("TAT by reference type").click()
        self.assertIn("TAT by reference", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_ActiveApplicants(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Active Applicants Report").click()
        self.assertIn("Active Applicants Report", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_ActiveApplicants(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Active Applicants Report").click()
        self.assertIn("Active Applicants Report", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_ActiveApplicants(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("LR Actions Report").click()
        self.assertIn("LR", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def test_LeadGeneration(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Lead Generation Report").click()
        self.assertIn("Lead Generation Report", driver.title)
        driver.find_element_by_name("sdate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_name("edate").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5000)

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()

