num = int(input("enter the number : "))
fact = 1
for i in range(num , 0, -1):
    fact = fact* i
    print(i, end = " ")

print(fact)