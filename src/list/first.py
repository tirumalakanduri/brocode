#shopping cart program


foods = []
prices = []
total = 0
tax = 0.0635

while True:
    food = input("enter a food to buy (q to quit) : ")
    if food  == "q" or food == "Q":
        break
    else:
        price = float(input(f"enter the price of a {food} : $"))
        foods.append(food)
        prices.append(price)

print("-------------your cart-------------")

for food in foods:
    print(food, end = " ")

for price in prices:
    total = total + price
    
tax_amount = total*tax
total_amount = total + tax_amount

print()
print(f"your total is : ${total_amount:.2f}")