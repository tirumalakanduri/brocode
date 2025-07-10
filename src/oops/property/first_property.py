#property = decorator used to define a method as a property (it can be accessed like an attribute)
#           Benfit: add additional logic when read, write or delete attributes
#           give you getter, setter and deleter method.
 

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):  # Getter
        return f"{self._width:.1f}cm"

    @width.setter
    def width(self, new_width):  # Setter
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than zero")

    @width.deleter
    def width(self):  # Deleter
        del self._width
        print("width has been deleted")

    @property
    def height(self):
        return f"{self._height:.1f}cm"

# Create an object
rectangle = Rectangle(3, 4)

# Access width and height
print(rectangle.width)   # prints: 3.0cm
print(rectangle.height)  # prints: 4.0cm

# Update width
rectangle.width = 5
print(rectangle.width)   # prints: 5.0cm

# Delete width using property deleter
del rectangle.width

# Try accessing width again (will raise an error if uncommented)
# print(rectangle.width)  # This will raise AttributeError
