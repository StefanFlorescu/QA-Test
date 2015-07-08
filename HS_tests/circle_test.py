__author__ = 'StefanFlorescu'

if __name__ == '__main__':


    from random import random, seed
    from DemoFiles.Circulitos import Circle

    seed(8675309)
    print("Using the circle class, version ",Circle.version )
    n= 20
    circles = [Circle(random()) for i in range(n)]
    print("The avereage area of ",n, " random circles is:")
    avg = sum([c.area for c in circles])/n
    print("%.1f"% avg)
    print()
#------------------------------------------------------------------------------
    from random import random, seed
    from DemoFiles.Circulitos import Circle

    cuts = [2,3,8]
    circles = [Circle(r) for r in cuts]
    for c in circles:
        print("A tier with radius of ", c.radius,": ")
        print("has a perimeter of ", c.perimiter)
        print("and has a cold area of ", c.area)
        c.radius *= 1.1
        print("and a warm area of ", c.area)
        print()
#------------------------------------------------------------------------------

from DemoFiles.Circulitos import Circle
class Tire(Circle):
    "This is a subclass of the Circle class - it inherits the class names"
    def perimiter(self):
        return Circle.perimiter *1.25


t = Tire.from_bbd(45)
print("a tire of radius ", t.radius)
print("has an iner area of ", t.area)
print("and an outermeter parametre of  ", t.perimiter)
