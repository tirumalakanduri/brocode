#conditional expression = a one line shortcut for the if else statement (ternary operator) 
# print or assign one of two values on a conditon 
# (X if conditon else Y)

num = 2
a = 6
b = 7
age = 13
temperature = 30
user_role = "guest"

print("positive" if num > 0 else "negative")

print("prime number" if num % 2 == 1 else "not prime number")
max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)
status = "adult" if age >= 18 else "child"
print(status)


even_odd = "even" if num % 2 == 0 else "odd"
print(even_odd)


weather = "hot " if temperature >= 35 else " cold"
print(weather)


access_level = "full access" if user_role == "admin" else "limited access"

print(access_level)