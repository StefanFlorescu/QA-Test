__author__ = 'StefanFlorescu'
from collections import OrderedDict


income_pool = {
    1: dict(type1=True, type2=False, name="Temporary/Contract Work",
            data=OrderedDict([("proof", ["select", "ContractDeliveryMethod", "Email"]),
                              ("employment", ["select", "employment_likely_to_change", "No"]),
                              ("employment_start", ["date", "EmploymentStartDate", "01/01/2015"]),
                              ("job_title", ["input", "JobTitle", "QA Manager"]),
                              ("company", ["input", "EmployersCompanyName", "Draytus"]),
                              ("referee_name", ["input", "RefereeName", "MainIncome EmployerTest Name"]),
                              ("referee_address", ["postcode", "PostCode", "ba133bn"]),
                              ("referee_number", ["input", "RefereeBusinessLandlineNumber", "3256458498"]),
                              ("referee_email", ["input","RefereeEmailAddress", "testinginbox11@draytus.net"]),
                              ("months_remained", ["select", "months_remaining", 36])])),

    2: dict(type1=True, type2=False, name="Part Time Employed",
            data=OrderedDict([("proof", ["select", "ContractDeliveryMethod", "Email"]),
                              ("employment", ["select", "employment_likely_to_change", "No"]),
                              ("employment_start", ["date", "EmploymentStartDate", "01/01/2015"]),
                              ("job_title", ["input", "JobTitle", "QA Manager"]),
                              ("company", ["input", "EmployersCompanyName", "Draytus"]),
                              ("referee_name", ["input", "RefereeName", "MainIncome EmployerTest Name"]),
                              ("referee_address", ["postcode", "PostCode", "ba133bn"]),
                              ("referee_number", ["input", "RefereeBusinessLandlineNumber", "3256458498"]),
                              ("referee_email", ["input","RefereeEmailAddress", "testinginbox12@draytus.net"])])),

    3: dict(type1=True, type2=True, name="Full time Employed",
            data=OrderedDict(proof=["select", "ContractDeliveryMethod", "Email"], employment=["select", "employment_likely_to_change", "No"],
                      employment_start=["date", "EmploymentStartDate", "01/01/2015"], job_title=["input", "JobTitle", "QA Manager"],
                      company= ["input", "EmployersCompanyName", "Draytus"], referee_name= ["input", "RefereeName", "MainIncome EmployerTest Name"],
                      referee_address=["postcode", "PostCode", "ba133bn"], referee_number=["input", "RefereeBusinessLandlineNumber", "3256458498"],
                      referee_email=["input","RefereeEmailAddress", "testinginbox13@draytus.net"])),

    4: dict(type1=True, type2=False, name="Self-Employed",
            data= OrderedDict(employed_time=["select", "SelfEmployedPeriod", 3], have_accountant=["select", "DoYouHaveAnAccountant", "Yes"],
                       firm_name=["input", "AccountancyFirmName", "Test Accountancy Firm"],referee_name=["input", "RefereeName", "MainIncome Self-employment Accountancy"],
                       referee_job=["input", "RefereeJobTitle", "QA Manager"], referee_address=["postcode", "PostCode", "ba133bn"],
                       referee_number=["input", "RefereeBusinessLandlineNumber", "78784654761"], referee_email=["input", "RefereeEmailAddress", "testinginbox14@draytus.net"])),

    5: dict(type1=True, type2=True, name = "Retired",
            data= dict(have_proof=["select", "DoYouHaveProofOfPension", "No"], pension_provider=["input", "PensionProviderName", "UK National Pension Fund"],
                       referee_name= ["input", "RefereeName", "MainIncome PensionTest"],referee_job=["input", "RefereeJobTitle", "Social Assistant"],
                       referee_address=["postcode", "PostCode", "ba133bn"], referee_phone=["input", "RefereeBusinessLandlineNumber", "879567831358"],
                       referee_email=["input", "RefereeEmailAddress", "testinginbox15@draytus.net"])),

    6: dict(type1=True, type2=True, name="Student sponsorship/funding",
            data= dict(delivery_method=["select", "DocumentDeliveryMethod", "Email"], funding_organisation=["input", "OrganisationName", "Oxford on Maine"],
                       referee_name=["input", "RefereeName", "MainIncome StudentTest"], referee_job=["input", "RefereeJobTitle", "Student Affairs manager"],
                       referee_address=["postcode", "PostCode", "ba133bn"], referee_phone=["input", "RefereeBusinessLandlineNumber", "879007831358"],
                       referee_email=["input", "RefereeEmailAddress", "testinginbox16@draytus.net"])),

    7: dict(type1=True, type2=True, name="Private Income",
            data= dict(who_toprovide=["select", "ReferenceProvider", "Solicitor"], referee_business=["input", "RefereeBusinessName", "Test Referee Business Name"],
                       referee_name=["input", "RefereeName", "MainIncome PrivateIncome"], referee_job=["input", "RefereeJobTitle", "General Manager"],
                       referee_address=["postcode", "PostCode", "ba133bn"], referee_phone=["input", "RefereeBusinessLandlineNumber", "899307831358"],
                       referee_email=["input", "RefereeEmailAddress", "testinginbox17@draytus.net"])),

    7: dict(type1=True, type2=True, name="Foster Carer Income",
            data= dict(who_toprovide=["select", "ReferenceProvider", "Agency"], referee_business=["input", "RefereeBusinessName", "Test Referee Business Name"],
                       referee_name=["input", "RefereeName", "MainIncome FosterIncome Test"], referee_job=["input", "RefereeJobTitle", "Financial Manager"],
                       referee_address=["postcode", "PostCode", "ba133bn"], referee_phone=["input", "RefereeBusinessLandlineNumber", "899307831358"],
                       referee_email=["input", "RefereeEmailAddress", "testinginbox17@draytus.net"]))
}

class Income(object):

    def __init__(self, income_number):
        self.income = income_pool[income_number]

    @property
    def get_type(self):
        return self.income["type"]

    @property
    def name(self):
        return self.income["name"]

    @property
    def data(self):
        return self.income["data"]
