__author__ = 'Steve'

class Person(object):

    def __init__(self):
        self.order = "animalia"
        self.branch = "vertebrates"

    def has_4members(self):
        return True

    def is_animal(self):
        if self.order != "plants":
            return True
        else:
            return False