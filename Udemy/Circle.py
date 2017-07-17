class Circle(object):
    pi = 3.14

    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return Circle.pi * (self.radius**2)

    def set_radius(self,radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def parimter(self):
        return 2 * Circle.pi * self.radius

