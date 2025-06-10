menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "popcorn" : 6.00,
        "fries" : 2.50,
        "chips" : 1.00,
        "pretzel" : 3.50,
        "soda" : 3.00,
        "lemonade" : 4.25}


cart = []

total = 0

print("----------menu--------------")
for key, value in menu.items():
    print(f"{key:10} : {value:.2f}") 

print("-----------------------------")

while True:
    food = input("select an item (q to quit) : ")
    if food == "q" or food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total = total + menu.get(food)
    print(food, end = " ")


print()
print(f"total is : ${total:.2f}")