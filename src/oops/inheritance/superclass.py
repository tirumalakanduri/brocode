#super() = Function used in a child class to call methods from a parent class(superclass).
#          Allows you to extend the functionality of the inherited methods.


class shape():
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not_filled'}")

class circle(shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"it is a circle with an area of {3.14 }")

class square(shape):
       def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class triangle(shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = circle(color = "red",filled = "yes", radius = 5)

square = square(color = "blue", filled = "no",width = 5 )
print(circle.color)
print(circle.filled)
print(f"{circle.radius}")
print(f"{square.width}")