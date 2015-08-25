from Automatisation.BasePage import BasePage

__author__ = 'StefanFlorescu'

class ApplicationForm(BasePage):

    def set_email(self):
        return str("testinginbox@{0}draytus.net".format(str(self.random_int(0, 10))))

    def action_alert(self, block_number):
        alert = self.wait_element(xpath='//div[@class="additional-income form-block clearfix" and @order={0}]/descendant::div[@class="message"]/p[2]/input[@value="Ok"]'.format(str(block_number)))
        alert.click()

    def set_applicat_personal_details(self, title="Mr", name = "Test", surename = "Test", sex = "Transgender", birth_date = "01/01/1990"):
        driver = self.driver
        driver.find_element_by_link_text("Application Information").click()
        self.select_option_byname("Title[]", title)
        applicant_name = driver.find_element_by_name("FirstName[]")
        applicant_name.clear()
        applicant_name.send_keys(name)
        applicant_surename = driver.find_element_by_name("Surname[]")
        applicant_surename.clear()
        applicant_surename.send_keys(surename)
        self.select_option_byname("Sex[]", sex)
        self.input_date_byname("DateOfBirth[]", birth_date)
        self.select_option_byname("HasPreviousSurnames[]", "No")
        self.select_option_byname("NumberOfDependants[]", 2)
        driver.find_element_by_name("Email[]").send_keys(self.set_email())
        self.select_option_byname("HasNationalInsuranceNumber[]", "No")
        self.select_option_byname("HasUKDrivingLicense[]", "No")
        self.select_option_byname("HasUKPassportNumber[]", "No")
        self.select_option_byname("HasAdverseData[]", "No")

    def set_maininc(self):
        self.driver.find_element_by_link_text("Application Information").click()
        self.select_option_byname("main_income_type", "Homemaker")
        self.wait()

    def set_addinc(self, incomes = 2):
        driver = self.driver

        for i in xrange(1, incomes+1):
            self.click_button_byvalue("Add additional income")
            locator = '//div[@class="additional-income form-block clearfix" and @order={0}]/descendant::'.format(str(i))
            self.select_optionbyxpath(locator+'select[@togglescope="#income-details"]', "Savings")

            self.action_alert(i)
            income_amount = driver.find_element_by_xpath(locator+'input[@class="additional_income_total"]')
            income_amount.clear()
            income_amount.send_keys(str(self.random_int(10000, 20000)))

    def set_address(self, applicant_addresses):
        driver = self.driver
        for i in applicant_addresses:
            if i != "" :
                address = driver.find_element_by_xpath('//div[id="address-history-details"]/div[id="item{0}"]'.format(str((i.index()))))
                address.send_keys(self.postcode)
                address.find_element_by_class_name("paf-lookup").click()
                self.set_address(i)









