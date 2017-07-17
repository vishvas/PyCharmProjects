import math
class Line(object):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor1[0]-self.coor2[0])**2 +(self.coor1[1]-self.coor2[1])**2)


    def slope(self):
        return (self.coor1[1]-self.coor2[1])/(self.coor1[0]-self.coor2[0])


class Cylinder(object):

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius**2) * self.height

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.height + self.radius )