__author__ = 'StefanFlorescu'

import math


class Circle(object):
    """An advanced circle analitic toolkit"""

    version = "0.1"  # this is a class variable - all the instances of this class share this variable

    def __init__(self, radius):
        self.radius = radius  # this is the "initializer function" that initiates the instance object of the class
        # - variables that can be used further in the class by invocation syntax "self.{variable_name}"

    @property
    def area(self):
        return math.pi * self.radius ** 2.0

    @property
    def perimiter(self):
        return 2.0 * math.pi * self.radius

    @classmethod
    def from_bbd(cls, bbd):  # alternative constructor
        """"Construct a circle from a bounding box diagonal - this is a constructor method"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)  # for a single class "return Circle(radius) works fine,
        # but for subclassing only "return cls(radius)" is appropriate

    @staticmethod
    def angle_to_grades(angle): # the staticmethod decorator attaches a function to the class tha uses no class name
        """ Conver angle in degrees to percentage grades"""
        return math.tan(math.radians(angle)) * 100.0




