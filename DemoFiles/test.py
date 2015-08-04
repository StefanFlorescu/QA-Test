__author__ = 'StefanFlorescu'

import random


class MyClass(object):
    def dothis(self):
        self.rand_val = random.randint(1,20)

myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)

print(); print();
