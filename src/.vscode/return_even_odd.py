# Check Even or Odd Using Function
#Write a function is_even(num) that returns True if the number is even, else returns False.
#Example: is_even(7) should return False.


def is_even(num):
    if num % 2 == 0:
        is_even = True
    else:
        is_even = False
    return is_even

print(is_even(2))