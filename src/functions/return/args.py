# *args = it allows to pass multiple non keyword arguments 
#          it collects them in tuple


def add(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total 

print(add(1, 2, 3, 4))









def  display_name(*args):
    for arg in args:
        print(arg, end = " ")

display_name("Mr.", "sudarshan", "sid")
