age = int(input("enter your age : "))

if age >= 100:
    print("you are too old to sign up")
elif age >= 18:
    print("you are now signed up!")
elif age < 0:
    print("you are not yet born!")
else:
    print("you must be 18+ to sign up")