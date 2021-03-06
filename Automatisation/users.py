__author__ = 'StefanFlorescu'

user_pool = dict(sandbox=dict(
    Letrisks=dict(manager=["Letrisks", "lr_manager@letrisks-acumen.com", "4cEfruzacr"],
                  area_manager=[],
                  branch_manager=[],
                  agent=["QA Test", "testinginbox@yahoo.com", "123456"],
                  operator=[]),
    Draytus=dict(manager=["QA Draytus", "draytus_manager@letrisks-acumen.com", "123456"],
                 area_manager=["QA Area Manager", "testingsitesqa@yandex.com", "123456"],
                 branch_manager=["QA Branch Manager", "testingsitesqa@outlook.com", "123456"],
                 agent=["Draytus Test", "testinginbox@gmail.com", "123456"],
                 operator=["QA Operator", "testingsitesqa@hotmail.com", "123456"]),
    API_Customer=dict(manager=[], area_manager=[],
                      branch_manager=[],
                      agent=["QA API Test", "testinginbox@yahoo.com", "123456"],
                      operator=[])),
    preprod=dict(
        Draytus=dict(manager=["QA Draytus", "draytus_manager@letrisks-acumen.com", "123456"],
               area_manager=["QA Area Manager", "testingsitesqa@yandex.com", "123456"],
               branch_manager=["QA Branch Manager", "testingsitesqa@outlook.com", "123456"],
               agent=["Draytus Test", "testinginbox@gmail.com", "123456"],
               operator=["QA Operator", "testingsitesqa@hotmail.com", "123456"])))


class User(object):
    def __init__(self, instance="letrisks", customer="Draytus", role="agent"):
        self.customer = customer
        if instance in "letrisks-acumen.com":
            self.branch = "None"
        elif instance in "sandbox.letrisks-acumen.com":
            self.branch = "Letrisks"
        else:
            self.branch = "et-1"
        self.role = role
        self.full_name = user_pool[self.customer][self.role][0]
        self.email = user_pool[self.customer][self.role][1]
        self.password_str = user_pool[self.customer][self.role][2]

    @property
    def username(self):
        return self.email

    @property
    def password(self):
        return self.password_str

    @property
    def name(self):
        return self.full_name

    def set_branch(self, branch):
        self.branch = branch
