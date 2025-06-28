#multi level inheritance : 
#

class Animal:   
    def __init__(self, name):
        self.name = name                       #grandparent class
    def eat(self):
        print(f"the {self.name} is eating")
    def sleep(self):
        print(f"this {self.name} is sleeping")

class prey(Animal):                            #parent class
    def flee(self):
        print(f"The {self.name} is fleeing!")

class predator(Animal):
    def hunt(self):
        print(f"The predator is hunting!")

class rabbit(prey):                     #child class
    pass

class hawk(predator):                    #child class
    pass

class fish(prey, predator):              #child class
    pass    


rabbit = rabbit("bugs")
hawk = hawk("tony")
fish = fish("nemo")

rabbit.sleep()
rabbit.eat()
fish.sleep()

hawk.flee()