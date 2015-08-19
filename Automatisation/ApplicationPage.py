from Automatisation.BasePage import BasePage

__author__ = 'StefanFlorescu'

class ApplicationPage(BasePage):

    def create_app(self):
        self.driver.find_element_by_partial_link_text("Tenancy Application").click()
        self.wait(1)
        self.driver.find_element_by_link_text("Create Application").click()
        self.wait(3)

    def set_branch(self, branch = "Letrisks"):
        self.select_option_byname("BranchId", branch)

    def set_agent(self, agent_name = "QA Test"):
        self.select_option_byname("AgentId", agent_name)

    def set_property(self):
        self.set_random_address(self.postcode)

    # def get_property(self):
    #     house_number = self.get_element_byngmodel("application.PropertyInformation.HouseNumber.Value").text
    #     flat_number = self.get_element_byngmodel("application.PropertyInformation.FlatNumber.Value").text
    #     house_name = self.get_element_byngmodel("application.PropertyInformation.HouseName.Value").text
    #     street_name = self.get_element_byngmodel("application.PropertyInformation.Street.Value").text
    #     town_name = self.get_element_byngmodel("application.PropertyInformation.Town.Value").text
    #     county_name = self.get_element_byngmodel("application.PropertyInformation.County.Value").text
    #     global tenancy_address
    #     tenancy_address = house_number+" "+house_name+" "+flat_number+" "+
    #     return


    def set_rental_details(self, rent=1000, term=12, start_date = "31/08/2015", frequency = "Monthly"):
        driver = self.driver
        rent_field = driver.find_element_by_id("ShareOfMonthlyRent")
        rent_field.clear()
        rent_field.send_keys(str(rent))
        driver.find_element_by_id("TenancyTerm").send_keys(term)
        driver.find_element_by_name("TenancyStartDate").send_keys(start_date)
        self.select_optionbyxpath('//select[@ng-model="application.RentalDetails.RentalFrequency.Value"]',frequency)


    def set_tenant(self, title = "Mr", first_name = "Tenant", surename = "Draytus", report_type = "Comprehensive", rent_share = 1000, order = 1):
        driver = self.driver
        driver.find_element_by_xpath("//input[@value='Add Tenant']").click()
        tenant_block = "//div[@id='tenantContainer']/div[contains(@ng-repeat,'filter:{IsGuarantor:false}')][%s]/descendant::"%order
        self.select_optionbyxpath(tenant_block + "select[@name='Title[]']", title)
        driver.find_element_by_xpath(tenant_block+"input[@ng-model='applicant.FirstName']").send_keys(first_name)
        driver.find_element_by_xpath(tenant_block+"input[@ng-model='applicant.Surname']").send_keys(surename)
        rent_field = driver.find_element_by_xpath(tenant_block+"input[@ng-model='applicant.ShareOfRent.Value']")
        rent_field.clear()
        rent_field.send_keys(rent_share)
        self.select_optionbyxpath(tenant_block+"select[@ng-model='applicant.ReportType.Value']", report_type)
        driver.find_element_by_xpath(tenant_block+"input[contains(@type, 'radio') and contains(@ng-value, 'false')]").click()
        self.select_optionbyxpath(tenant_block+"select[@ng-model='applicant.ApplicantPayingInAdvance.Value']", "No")


    def set_guarantor(self, title = "Mr", first_name = "Guarantor", surename = "Draytus", report_type = "Comprehensive", rent_share = 1000, order = 1):
        driver = self.driver
        driver.find_element_by_xpath("//input[@value='Add Guarantor']").click()
        guarantor_block = "//div[@id='guarantorContainer']/div[contains(@ng-repeat,'filter:{IsGuarantor:true}')][%s]/descendant::"%order
        self.select_all_byxpath(guarantor_block+"select[@ng-model='applicant.Applicants']")
        self.select_optionbyxpath(guarantor_block + "select[@name='Title[]']", title)
        driver.find_element_by_xpath(guarantor_block+"input[@ng-model='applicant.FirstName']").send_keys(first_name)
        driver.find_element_by_xpath(guarantor_block+"input[@ng-model='applicant.Surname']").send_keys(surename)
        self.select_optionbyxpath(guarantor_block+"select[@ng-model='applicant.ReportType.Value']", report_type)
        driver.find_element_by_xpath(guarantor_block+"input[contains(@type, 'radio') and contains(@ng-value, 'false')]").click()
