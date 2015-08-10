from Automatisation.BasePage import BasePage

__author__ = 'StefanFlorescu'

class ApplicationPage(BasePage):

    def set_branch(self, branch = "None"):
        self.select_option_byname("BranchId", branch)

    def set_agent(self, agent_name = "QA Test"):
        self.select_option_byname("AgentId", agent_name)

    def set_property(self, postcode = "IV44 8TZ"):
        self.random_address(postcode)

    def set_rental_details(self, rent, term, start_date = "31/08/2015"):
        driver = self.driver
        rent = driver.find_element_by_id("ShareOfMonthlyRent")
        rent.clear()
        # rent.send_keys(rent)
        driver.find_element_by_id("TenancyTerm").send_keys(term)
        driver.find_element_by_name("TenancyStartDate").send_keys(start_date)


    def set_tenant(self, title, first_name, surename, report_type, rent_share):
        driver = self.driver
        driver.find_element_by_xpath("//input[@value='Add Tenant']").click()
        self.select_option_byngmodel("applicant.Title.Value", title)
        driver.find_element_by_xpath("//input[@ng-model='applicant.FirstName']").send_keys(first_name)
        driver.find_element_by_xpath("//input[@ng-model='applicant.Surname']").send_keys(surename)
        driver.find_element_by_xpath("//input[@ng-model='applicant.ShareOfRent.Value']").send_keys(rent_share)
        driver.find_element_by_xpath("//input[contains(@type, 'radio') and contains(@ng-value, 'false')]").click()
        self.select_option_byngmodel("applicant.ApplicantPayingInAdvance.Value", "No")



