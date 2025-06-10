number = int(input("enter the number : "))
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10

print(f"sum of digits = { sum }")