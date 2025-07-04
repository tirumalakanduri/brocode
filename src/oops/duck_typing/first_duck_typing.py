#Duck typing = another way to achieve polymorphism besides inheritance
#              object must have the minimum necessary attributes/ methods
#             "if it looks like a duck and quacks like a duck, it must be a duck"



class Animal:
    alive = True

class dog(Animal):
    def speak(self):
       print("woof!") 


class cat(Animal):
    def speak(self):
        print("Meow!")


class car:
    alive = False
    def speak(self):
        print("honk!")


animals = [dog(), cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)