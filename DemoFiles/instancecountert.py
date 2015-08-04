_author__ = 'StefanFlorescu'

class InstanceCounter (object):

    count = 0
    def __init__(self, val):
        self.value = val
        InstanceCounter.count +=1

    def set_val(self, newvalue):
        self.value = newvalue

    def get_val(self):
        return self.value

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a,b,c):
    print "val of object %s" % (obj.get_val())
    print "count from instance %s" % (obj.get_count())
    print obj.count
