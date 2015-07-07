__author__ = 'StefanFlorescu'


class Circle(object):
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


class Widjet(object):
    copy = "StefanFlorescu. Inc"


class Circle2(Widjet):
    pi = 3.15

    def __init__(self, radius):
        self.radius = radius

    @property
    def circumference(self):
        return 2 * self.radius * self.pi


class MyDescriptors(object):
    def __get__(self, obj, type):
        print(self, obj, type)
    def __set__(self, obj, val):
        print("Got %s" % val)

class MyClass(object):
    x = MyDescriptors()


def add_by(x):
    return lambda y:y+x

for i in range(50):
    print (i**i)
