import random


"┌─────────┐"
"│         │"
"│    ●    │"           #using the uni codes i made this dice. 
"│         │"
"└─────────┘"

dice_art =  {1 : ("┌─────────┐", 
                  "│         │",
                  "│    ●    │", 
                  "│         │", 
                  "└─────────┘"),
             2 : ("┌─────────┐", 
                  "│  ●      │",
                  "│         │", 
                  "│      ●  │", 
                  "└─────────┘"),
             3 : ("┌─────────┐", 
                  "│ ●       │",
                  "│    ●    │", 
                  "│       ● │", 
                  "└─────────┘"),
             4 : ("┌─────────┐", 
                  "│ ●    ●  │",
                  "│         │", 
                  "│ ●    ●  │", 
                  "└─────────┘"),
             5 : ("┌─────────┐", 
                  "│ ●     ● │",
                  "│    ●    │", 
                  "│ ●     ● │", 
                  "└─────────┘"),
             6 : ("┌─────────┐", 
                  "│ ●     ● │",
                  "│ ●     ● │", 
                  "│ ●     ● │", 
                  "└─────────┘")}


dice = []
total = 0
number_of_dice = int(input("enter how many dice : "))

for die in range(number_of_dice):
    dice.append(random.randint(1, 6))

for die in range(number_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f"total: {total}")