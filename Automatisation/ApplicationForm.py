from Automatisation.BasePage import BasePage

__author__ = 'StefanFlorescu'

class ApplicationForm(BasePage):

    def set_email(self):
        return str("testinginbox{0}@draytus.net".format(str(self.random_int(1, 10))))

    def action_alert(self, block_number):
        alert = self.wait_element(xpath='//div[@class="additional-income form-block clearfix" and @order={0}]/descendant::div[@class="message"]/p[2]/input[@value="Ok"]'.format(str(block_number)))
        alert.click()

    def set_applicat_personal_details(self, title="Mr", name = "Test", surename = "Test", sex = "Transgender", birth_date = "01/01/1990", nationality = "British",
                                      marital_status="Single"):
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
        self.set_date("DateOfBirth[]", birth_date)
        self.select_option_byname("Nationality[]", nationality)
        self.select_option_byname("MaritalStatus[]", marital_status)
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
            self.select_option_byxpath(locator+'select[@togglescope="#income-details"]', "Savings")

            self.action_alert(i)
            income_amount = driver.find_element_by_xpath(locator+'input[@class="additional_income_total"]')
            income_amount.clear()
            income_amount.send_keys(str(self.random_int(10000, 20000)))

    def set_address_history(self, applicant_addresses):
        driver = self.driver.find_element_by_id("address-history-details")
        self.driver.find_element_by_link_text("Address History").click()
        for i in applicant_addresses:
            if i != "":
                driver.find_element_by_xpath('//div[@id="address-history-details"]/descendant::a[@href="#item{0}"]'.format(applicant_addresses.index(i)+1)).click()
                address = driver.find_element_by_xpath('//div[@id="address-history-details"]/div[@id="item{0}"]'.format(str((applicant_addresses.index(i)+1))))
                postcode_field = "address_record_{0}_PostCode".format(applicant_addresses.index(i))
                self.set_address(postcode_field, i)

    def set_bank_details(self):
        self.driver.find_element_by_link_text("Bank Details").click()
        driver = self.driver.find_element_by_id("bank-details")
        self.select_option_byname("CreditCardCount", self.random_int(1, 4))
        self.select_option_byname("DoYouHaveUKCurrentAccount", "No")


    def set_nextofkin(self):
        self.driver.find_element_by_link_text("Next Of Kin").click()
        driver = self.driver.find_element_by_id("nextofkin-details")
        driver.find_element_by_name("NextOfKin_FirstName").send_keys("Test Name")
        driver.find_element_by_name("NextOfKin_Surname").send_keys("Test Surename")
        driver.find_element_by_name("NextOfKin_Relationship").send_keys("Brother")
        self.set_randomaddress("NextOfKin_PostCode")
        driver.find_element_by_name("NextOfKin_MobileTelephoneNumber").send_keys("13264875679")
        driver.find_element_by_name("NextOfKin_HomeTelephoneNumber").send_keys("0984868546")
        driver.find_element_by_name("NextOfKin_EmailAddress").send_keys("testinginbox29@draytus.net")

    def set_additional_details(self):
        self.driver.find_element_by_link_text("Additional Information").click()
        self.select_option_byname("WillThereBeAnyPets", "No")
        self.select_option_byname("WillAnyOfTenantsSmoke", "No")
        child_count = self.random_int(0, 7)
        self.select_option_byname("ChildrenCount", child_count)
        if child_count > 0:
            for i in xrange(1, child_count+1):
                driver = self.driver.find_element_by_xpath('//div[@class="child"][{0}]'.format(i))
                driver.find_element_by_name("children-FirstName[]").send_keys("Test_child_{0}".format(i))
                driver.find_element_by_name("children-Surname[]").send_keys("Test_surename")















