#Decorator = A function that extends the behivour of another function.
#            without modifying the base function
#            pass the base function as an argument to the decortor.


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("you add a fudge")
        func(*args, **kwargs)
    return wrapper
    
@add_fudge    
@add_sprinkles
def get_ice_cream(flavour):
    print(f"here is your {flavour}ice cream ")


get_ice_cream("vanilla")