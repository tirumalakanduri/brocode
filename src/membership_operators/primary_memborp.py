# membership operators = used to test weather a value or variable is found in a sequence 
#                        (string, list, tuple, set or dictionay)
#                         1. in
#                         2. not in 



word = "APPLE"
letter = input("guess a letter in the secret word : ")

if letter in word:
    print(f"There is a {letter }")
else:
    print(f"{letter} was not found")