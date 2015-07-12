__author__ = 'Steve'


class Complex(object):

    def __init__(self, real=1, imaginary=2):
        self.real = real
        self.imaginary = imaginary

    @property
    def real_part(self):
        return self.real

    @property
    def imaginary_part(self):
        return self.imaginary

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

