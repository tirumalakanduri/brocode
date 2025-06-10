number = int(input("enter the number : "))
reversed = 0
while number > 0:
    digit = number % 10
    reversed = reversed *10 + digit
    number //= 10
print(f"reversed number = {reversed}")