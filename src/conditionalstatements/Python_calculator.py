operator = input("enter your operator ( + , - , / , *) : ")
if operator == "+" or operator == "-" or operator == "/" or operator == "*":
    num_1 = float(input(" enter the first number : "))
    num_2 = float(input(" enter the second number : "))
    if operator == "+":
        addition = num_1 + num_2
        print(f" you have selected addition and the result is {round(addition, 3)}")
    elif operator == "-":
        subtraction = num_1 - num_2
        print(f" you have selected subtraction and the result is { round(subtraction, 3)}")
    elif operator == "*":
        multiplication = num_1 * num_2
        print(f" you have selected multiplication and the result is {round(multiplication, 3)}")
    elif operator == "/":
        divison = num_1 / num_2
        print(f" you have selected divison and the result is { round(divison, 3)}")
else:
    print(" please enter in among +-*/")

