rows = int(input("enter the rows : "))
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end = " " )
    print()