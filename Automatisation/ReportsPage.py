
from Automatisation.BasePage import BasePage

class CreatePage(BasePage):
    pass

class StatReports(BasePage):

    def test_CSVreport(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("CSV").click()
        assert "CSV Report" in driver.title
        BasePage.set_date(self)
        driver.find_element_by_name("build").click()

    def test_OverallTAT(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("TAT").click()
        assert "TAT" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_LandlordReport(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("The Landlord").click()
        assert "Landlord" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_ReferenceVolumes(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Reference Volumes").click()
        assert "Reference Volumes" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()



    def test_ReferenceDecisions(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Reference Decisions").click()
        assert "Reference Decisions" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_RefereeResponse(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Referee Response").click()
        assert "Referee Response" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_IncomingCommunications(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Incoming Communications").click()
        assert "Incoming Communications" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_EquifaxData(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Equifax data").click()
        assert "Equifax Data Request" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_UserActivity(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("User Activity Report").click()
        assert "User Activity Report" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_TATbyReference(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("TAT by reference type").click()
        assert "TAT by reference type" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_ActiveApplicants(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Active Applicants Report").click()
        assert "Active Applicants Report" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_ActiveApplicants(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Active Applicants Report").click()
        assert "Active Applicants Report" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()


    def test_ActiveApplicants(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("LR Actions").click()
        assert "LR" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()
        driver.implicitly_wait(5)


    def test_LeadGeneration(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Lead Generation Report").click()
        assert "Lead Generation" in driver.title
        BasePage.set_startdate(self)
        BasePage.set_enddate(self)
        driver.find_element_by_name("build").click()




