import Automatisation

__author__ = 'StefanFlorescu'
from Automatisation.BasePage import BasePage
from Automatisation.Incomes import income_pool



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
        self.select_option_byname(driver, "Title[]", title)
        applicant_name = driver.find_element_by_name("FirstName[]")
        applicant_name.clear()
        applicant_name.send_keys(name)
        applicant_surename = driver.find_element_by_name("Surname[]")
        applicant_surename.clear()
        applicant_surename.send_keys(surename)
        self.select_option_byname(driver, "Sex[]", sex)
        self.set_date(driver, "DateOfBirth[]", birth_date)
        self.select_option_byname(driver, "Nationality[]", nationality)
        self.select_option_byname(driver, "MaritalStatus[]", marital_status)
        self.select_option_byname(driver, "HasPreviousSurnames[]", "No")
        self.select_option_byname(driver, "NumberOfDependants[]", 2)
        driver.find_element_by_name("Email[]").send_keys(self.set_email())
        self.select_option_byname(driver, "HasNationalInsuranceNumber[]", "No")
        self.select_option_byname(driver, "HasUKDrivingLicense[]", "No")
        self.select_option_byname(driver, "HasUKPassportNumber[]", "No")
        self.select_option_byname(driver, "HasAdverseData[]", "No")

    def set_maininc(self, income_object):
        self.driver.find_element_by_link_text("Income Details").click()
        self.select_option_byname(self.driver, "main_income_type", income_object.name)
        driver = self.wait_element(20, "//div[@id='d-sections']/div[@class='column-group']")
        print("the webelement has been identified at "+str(id(driver)))
        print(type(driver))
        self.complete_fields(driver, income_object.data)

    def complete_fields(self, driver, income_dict):
        fields = income_dict
        for element in fields:
            selector= fields[element][0]
            if selector == "input":
                input = driver.find_element_by_xpath('//input[starts-with(@name,\"{0}\")]'.format(fields[element][1]))
                input.send_keys(str(fields[element][2]))
            if selector== "select":
                self.select_option_byxpath(driver, '//select[starts-with(@name,\"{0}\")]'.format(fields[element][1]), str(fields[element][2]))
            if selector== "date":
                self.set_date(driver, fields[element][1], fields[element][2])
            if selector== "postcode":
                self.set_randomaddress(fields[element][1])



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
        child_count = self.random_int(0, 3)
        self.select_option_byname("ChildrenCount", child_count)
        if child_count > 0:
            for i in xrange(1, child_count+1):
                driver = self.driver.find_element_by_xpath('//div[@class="child"][{0}]'.format(i))
                driver.find_element_by_name("children-FirstName[]").send_keys("Test_child_{0}".format(i))
                driver.find_element_by_name("children-Surname[]").send_keys("Test_surename")



