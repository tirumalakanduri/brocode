#super() = Function used in a child class to call methods from a parent class(superclass).
#          Allows you to extend the functionality of the inherited methods.


class shape():
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class circle(shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

class square(shape):
       def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class triange(shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = circle(color = "red",filled = "yes", radius = 5)
print(circle.color)