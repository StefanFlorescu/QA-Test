import random

__author__ = 'StefanFlorescu'

class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" %(self.name, food))

class Dog_simple(Animal):

    def fetch(self, thing):
        print("%s is going after the %s" %(self.name, thing))

# d = Dog_simple("feggi")
# print(d.name)

class Dog(Animal):

    def __init__(self,klicika):
        super(Dog,self).__init__(klicika)
        self.breed = random.choice(["pichichao","mutt","ofcerca"])

    def featch(self,thing):
        print "%s goes after the %s" % (self.name, thing)

d = Dog("rockie")
print d.name
print d.breed