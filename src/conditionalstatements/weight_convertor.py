
unit = input("enter your weight in kilograms or pounds (K or L) : ")
if unit == "K" or unit == "k" or unit == "L" or unit == "l":
    weight = float(input("enter your present weight : "))
    if unit == "K" or unit == "k":
        weight = weight * 2.205
        print(f"your weight is {round(weight, 2)} kgs ")
    elif unit == "L" or unit == "l":
        weight = weight / 2.205
        print(f"your weight is {round(weight, 2)} lbs")   
else:
    print("please select between k,K,L,l")


