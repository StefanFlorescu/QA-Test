__author__ = 'StefanFlorescu'


from Automatisation.raw_data import user_pool

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

    def branch(self, branch):
        return self.user[3]


