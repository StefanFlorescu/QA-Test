__author__ = 'StefanFlorescu'

from Automatisation.users_pool import mass
import random


class User(object):
    def __init__(self, ccj_value=False, phone_value=False):

        def user_index():
            """ func that returns the index of the object that meets the initializator variable values(requirements)
            :return: int
            """
            while True:
                index = random.randint(0, mass.__len__() - 1)
                if mass[index]["ccj"] == ccj_value and mass[index]["phone"] == phone_value:
                    break
                return index

        self.selector = user_index()
        self.name = mass[self.selector]["name"][0]
        self.surename = mass[self.selector]["name"][1]
        self.birthdate = mass[self.selector]["name"][2]
        self.address1 = mass[self.selector]["address"][0]
        self.address2 = mass[self.selector]["address"][1]
        self.address3 = mass[self.selector]["address"][2]
        self.sort_code = mass[self.selector]["bank"][0]
        self.account = mass[self.selector]["bank"][1]
        self.title = mass[self.selector]["details"][0]
        self.sex = mass[self.selector]["details"][1]
        self.origin = mass[self.selector]["details"][2]
        self.status = mass[self.selector]["details"][3]


x = User()
print(x.__dict__ )
