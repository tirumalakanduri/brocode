#polymorphism = Greek word that means to "have many form of faces
#                 poly = many
#                 morphe = form

#           two types to achieve polymorphism
#           1. Inheritance = An object could be treated of the same type asa parent class
#           2. "Duck Typing" = object must have necessary attributes/ methods

#     It is the ability of different classes to be treated as instances of the same class through
#     a common interface. This is typically used when different objects (from different classes)
#     implement the same method name but behave differently.


from abc import ABC, abstractmethod
class shape:

    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class pizza(circle):
    def __init__(self, radius):
        super().__init__(radius)
        


shapes = [circle(4), square(5), triangle(6,7), pizza(101)]

for shape in shapes:
    print(f"{shape.area()}cm2")