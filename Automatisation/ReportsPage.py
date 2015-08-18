from Automatisation.BasePage import BasePage

class StatReports(BasePage):

    def access_report(self, report):
        self.goto_menuoption(partial_text=report)

    def make_referencedirectory(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('Reference').click()
        self.wait()
        driver.find_element_by_link_text("Reference directory").click()
        assert "directory" in self.title
        self.set_randomoption('filter[IncomeType]')
        self.trigger_filter()
        self.wait()

    def make_csvreport(self):
        self.access_report("Daily billing CSV")
        assert "CSV Report" in self.driver.title
        self.set_singledate()
        self.click_button()
        self.wait()

    def make_overalltat(self):
        self.access_report("Overall TAT")
        assert "TAT" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()


    def make_landlordreport(self):
        self.access_report("Who Is The Landlord Report")
        assert "Landlord" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_activetasksreport(self):
        self.access_report("Active Tasks")
        assert "Active Tasks" in self.title
        self.set_startdate()
        self.set_enddate()
        self.set_randomoption("customer")
        self.wait()
        self.select_all("branches[]")
        self.click_button()
        self.wait()

    def make_referencevolreport(self):
        self.access_report("Reference Volumes")
        assert "Reference Volumes" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()


    def make_refdecisionreport(self):
        self.access_report("Reference Decisions")
        assert "Reference Decisions" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_refresponsereport(self):
        self.access_report("Referee Response")
        assert "Referee Response" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_incomcommreport(self):
        self.access_report("Incoming Communications")
        assert "Incoming Communications" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_equifaxdatasearchreport(self):
        self.access_report("Equifax data")
        assert "Equifax Data Request" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_tenantacceptsreport(self):
        self.access_report("Daily Tenant")
        assert "Daily Tenant" in self.title
        self.set_singledate()
        self.click_button()
        self.wait()

    def make_tenantprofilereport(self):
        self.access_report("Tenant Profile")
        assert "Tenant Profile" in self.title
        self.set_startdate()
        self.set_enddate()
        self.set_randomoption("customer")
        self.wait(2)
        self.select_all("branches[]")
        self.click_button()
        self.wait()

    def make_useractivityreport(self):
        self.access_report("User Activity Report")
        assert "User Activity Report" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_tatbyrefreport(self):
        self.access_report("TAT by reference type")
        assert "TAT by reference" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_activeapplicantsreport(self):
        self.access_report("Active Applicants Report")
        assert "Active Applicants Report" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_activeappllicantsreport(self):
        self.access_report("Active Applicants Report")
        assert "Active Applicants Report" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_leadgenerationreport(self):
        self.access_report("Lead Generation Report")
        assert "Lead Generation" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()

    def make_refturnaroundreport(self):
        self.access_report("Reference Turnaround")
        assert "Reference Turnaround" in self.title
        self.set_startdate("cdate")
        self.set_enddate("sdate")
        self.wait()
        self.select_all("RMethod[]")
        self.click_button()
        self.wait()

    def make_actionsreport(self):
        self.access_report("LR Actions")
        assert "LR" in self.title
        self.set_startdate()
        self.set_enddate()
        self.click_button()
        self.wait()




