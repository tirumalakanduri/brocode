rows = int(input("enter the rowns: "))
columns = int(input("enter the columns : "))
symbol = input("which symbol you want to use : ")

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if i == 1 or i == rows or j == 1 or j == columns :
            print(symbol, end = " ")
        else:
            print(" ", end = " ")
    
    print()