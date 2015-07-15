from Automatisation.BasePage import BasePage




class CreatePage(BasePage):



class StatReports(BasePage):

    def test_ReferenceDirectory(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Reference').click()
        driver.find_element_by_link_text('Reference directory').click()
        assert "directory" in driver.title
        BasePage.set_randomoption(self, 'filter[IncomeType]')
        self.trigger_filter()
        self.wait()

    def test_CSVreport(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Daily billing").click()
        assert "CSV Report" in driver.title
        BasePage.set_date(self)
        driver.find_element_by_name("build").click()
        self.wait()

    def test_OverallTAT(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("TAT").click()
        assert "TAT" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_LandlordReport(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("The Landlord").click()
        assert "Landlord" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()

    def test_ActiveTasks(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Active Tasks ").click()
        assert "Active Tasks" in driver.title
        self.set_startdate()
        self.set_enddate()
        self.set_randomoption("customer")
        self.wait()
        self.select_all("branches[]")
        driver.find_element_by_name("build").click()
        self.wait()



    def test_ReferenceVolumes(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Reference Volumes").click()
        assert "Reference Volumes" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_ReferenceDecisions(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Reference Decisions").click()
        assert "Reference Decisions" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_RefereeResponse(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Referee Response").click()
        assert "Referee Response" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_IncomingCommunications(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Incoming Communications").click()
        assert "Incoming Communications" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_EquifaxDataSearch(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Equifax data").click()
        assert "Equifax Data Request" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()

    def test_TenantsAccepts(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Daily Tenant").click()
        assert "Daily Tenant" in driver.title
        self.set_date()
        driver.find_element_by_name("build").click()
        self.wait()

    def test_TenantProfile(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Tenant Profile").click()
        assert "Tenant Profile" in driver.title
        self.set_startdate()
        self.set_enddate()
        self.set_randomoption("customer")
        self.wait()
        self.select_all("branches[]")
        driver.find_element_by_name("build").click()
        self.wait()

    def test_UserActivity(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("User Activity Report").click()
        assert "User Activity Report" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_TATbyReference(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("TAT by reference type").click()
        assert "TAT by reference" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_ActiveApplicants(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Active Applicants Report").click()
        assert "Active Applicants Report" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_ActiveApplicants(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Active Applicants Report").click()
        assert "Active Applicants Report" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()


    def test_LeadGeneration(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Lead Generation Report").click()
        assert "Lead Generation" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()

    def test_ReferenceTurnaround(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("Reference Turnaround").click()
        assert "Reference Turnaround" in driver.title
        self.set_startdate()
        self.set_enddate()
        self.set_randomoption("customer")
        self.wait()
        self.select_all("RMethod[]")
        driver.find_element_by_name("build").click()
        self.wait()

    def test_ActionsReport(self):
        driver = self.driver
        driver.find_element_by_link_text("MI").click()
        driver.find_element_by_partial_link_text("LR Actions").click()
        assert "LR" in driver.title
        self.set_startdate()
        self.set_enddate()
        driver.find_element_by_name("build").click()
        self.wait()




