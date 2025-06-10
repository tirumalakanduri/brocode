#variable scope = where a variable is visible and accessible 
#scope resolution = (LEGB) LOCAL -> ENCLOSED -> GLOBAL -> BUILT-IN


def fun1():
    a = 1 
    print(a)

def fun2():
    b = 2
    print(b)