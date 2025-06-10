#validate user input exercise
# username is no more than 12 chareacters
# unsername must contain spaces
# username must not contain digits

user_name = input("enter the user name : ")


if len(user_name) > 12:
    print("your user name should not exceed more than 12 characters")
elif not user_name.find(" ") == -1:
    print("your user name can't contain spaces")
elif not user_name.isalpha():
    print("your user name should not contain numbers")
     
else:
    print(f"welcome {user_name}!") 