# 5. Check if a Number is Prime
# Create a function is_prime(n) that returns True if the number is prime, otherwise returns False.
# Use a for loop and conditions inside the function to implement it.
# Example: is_prime(11) should return True.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



print(is_prime(5))
print(is_prime(2))
print(is_prime(4))
print(is_prime(6))
print(is_prime(7))
print(is_prime(11))

