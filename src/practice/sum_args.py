# Multi-Argument Adder (Function + args)
# Write a function add_all(*args) that takes any number of numeric arguments and returns their total sum.
# Example: add_all(1, 2, 3, 4) → 10

def sum_args(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum_args(1, 2, 3, 4))