__author__ = 'StefanFlorescu'

user_pool = dict(

    sandbox=dict(
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

    preprod= dict( Draytus=dict(manager=["QA Draytus", "draytus_manager@letrisks-acumen.com", "123456"],
                 area_manager=["QA Area Manager", "testingsitesqa@yandex.com", "123456"],
                 branch_manager=["QA Branch Manager", "testingsitesqa@outlook.com", "123456"],
                 agent=["Draytus Test", "testinginbox@gmail.com", "123456"],
                 operator=["QA Operator", "testingsitesqa@hotmail.com", "123456"])),

    testing = dict(Draytus=dict(manager=["QA Draytus", "draytus_manager@letrisks-acumen.com", "123456"],
                 area_manager=["QA Area Manager", "testingsitesqa@yandex.com", "123456"],
                 branch_manager=["QA Branch Manager", "testingsitesqa@outlook.com", "123456"],
                 agent=["Draytus Test", "testinginbox@gmail.com", "123456"],
                 operator=["QA Operator", "testingsitesqa@hotmail.com", "123456"]))
)


class User(object):
    def __init__(self, instance="preprod", customer="Draytus", role="agent"):
        self.user = user_pool[instance][customer][role]
        if instance in "sandbox.letrisks-acumen.com":
            self.branch = "Letrisks"
        elif instance in "letrisks-acumen.com":
            self.branch = "None"
        else:
            self.branch = "et-1"


    @property
    def role(self):
        return self.role

    @property
    def username(self):
        return self.user[1]

    @property
    def password(self):
        return self.user[2]

    @property
    def reporter_name(self):
        return self.user[0]

    def set_branch(self, branch):
        self.branch = branch


