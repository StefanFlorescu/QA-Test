__author__ = 'StefanFlorescu'


income_pool = {
    1: dict(type="main_income", type2=None, name="Temporary/Contract Work",
            data=dict(proof=["select", "ContractDeliveryMethod", "Email"], employment=["select", "employment_likely_to_change", "No"],
                      employment_start=["date", "EmploymentStartDate", "01/01/2015"], job_title=["input", "JobTitle", "QA Manager"],
                      company= ["input", "EmployersCompanyName", "Draytus"], referee_name= ["input", "RefereeName", "EmployerTest Name"],
                      referee_address=["postcode", "PostCode", "ba133bn"], referee_number=["input", "RefereeBusinessLandlineNumber", "3256458498"],
                      referee_email=["input","RefereeEmailAddress", "testinginbox11@draytus.net"], months_remained=["select", "months_remaining", 36]))
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
