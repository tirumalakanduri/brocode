number = int(input("enter the number : "))

original = number 

reversed = 0
while number > 0:
    digit = number % 10
    reversed = reversed * 10 + digit
    number //= 10

if original == reversed:
    print(" the number you have entered is a palindrome ")
else:
    print("the number you have entered is not a palindorme.")