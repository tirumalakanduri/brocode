#multiple_inheritance = one child class  inherit from one or more parent classes
#                      c(A,B)

class prey:
    def flee(self):
        print("The animal is fleeing!")

class predator:
    def hunt(self):
        print("The predator is hunting!")

class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey, predator):
    pass    


rabbit = rabbit()
hawk = hawk()
fish = fish()

rabbit.flee()  # The animal is fleeing!
hawk.hunt()

fish.flee()
fish.hunt()