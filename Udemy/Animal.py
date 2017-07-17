class Animal(object):

    def __init__(self):
        print("Animal Class Defined")

    def whoAmI(self):
        print("Animal")

    def eating(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Class Created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof ")

    def __str__(self):
        return "This is a Dog"