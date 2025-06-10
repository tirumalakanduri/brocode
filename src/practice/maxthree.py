#Find Maximum of Three Numbers
#Write a function max_of_three(a, b, c) that takes three numbers and returns the largest one using conditional statements.
#Example: max_of_three(4, 9, 2) should return 9

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(max_of_three(4, 9, 9.1))