name = input("enter your full name: ")
phone_number = int(input("enter your phone number : "))
result = len(name)
result = name.find("o")    # here in the find function the result will be given in index numbers.
result = name.rfind("q")     # here we took input as brocode and in string brocode there is no letter q so thats why the result will be -1.

name = name.capitalize() # here the first letter in the string input like which you give the first letter in it will be capitalized.

name = name.upper() # all the characters in the string are capital

name = name.lower() # all the characters in the string are lowercase

name = name.isdigit()  #  here if you give input a number then the result will be true

result = name.isalpha()  # here if the given input has alphabets the output will be true
print(result)
result = phone_number.count()

