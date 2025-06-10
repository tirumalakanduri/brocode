item = input(" what item you would like to buy?: ")
price = float(input(" what is the price? : "))
quantity = int(input( " how many would you like? :  " ))

total = price * quantity
print(f"you have bought {quantity} X {item}/s")

print(f"your total is: ${total}")