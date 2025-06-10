#sum of the digit

num = int(input("enter the number : "))

sum_of_digit = 0

while num > 0:
    digit = num % 10
    sum_of_digit += digit
    num = num // 10

print(f"sum of digit {sum_of_digit}")