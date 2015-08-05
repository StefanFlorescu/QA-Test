__author__ = 'StefanFlorescu'

user_pool = {'Letrisks': dict(manager=["Letrisks", "lr_manager@letrisks-acumen.com", "4cEfruzacr"], area_manager=[],
                              branch_manager=[], agent=["QA Test", "testinginbox@yahoo.com", "123456"], operator=[]),
             'Draytus': dict(manager=["QA Draytus", "draytus_manager@letrisks-acumen.com", "123456"],
                             area_manager=["QA Area Manager", "testingsitesqa@yandex.com", "123456"],
                             branch_manager=["QA Branch Manager", "testingsitesqa@outlook.com", "123456"],
                             agent=["QA Test", "testinginbox@yahoo.com", 123456],
                             operator=["QA Operator", "testingsitesqa@hotmail.com", "123456"]),
             'API_Customer': dict(manager=[], area_manager=[],
                                  branch_manager=[], agent=["QA API Test", "testinginbox@yahoo.com", "123456"],
                                  operator=[])}


class User(object):
    def __init__(self, customer="Draytus", role="agent"):
        if user_pool.has_key(customer):
            self.customer = customer
            self.role = role
            self.name = user_pool[customer][role][0]
            self.email = user_pool[customer][role][1]
            self.password = user_pool[customer][role][2]
        else:
            self.customer = "Letrisks"
            self.role = role
            self.name = user_pool[customer][role][0]
            self.email = user_pool[customer][role][1]
            self.password = user_pool[customer][role][2]