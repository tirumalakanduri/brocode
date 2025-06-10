#reverse of a number

num = int(input("enter a number : "))

reversed = 0

while num > 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num = num // 10

print(f"reversed = {reversed}")