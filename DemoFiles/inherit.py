__author__ = 'Steve'

from DemoFiles.initializator import Complex


class Number(Complex):
    t = "real and integer part "

    def show(self):
        print(self.t + self.real + " " + self.imaginary)