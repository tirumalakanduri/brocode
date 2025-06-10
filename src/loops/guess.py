secret_number = 7

guess = int(input("guess the number : "))

while guess != secret_number:
    print(" the number you are guessing is not correct so guess again")
    guess = int(input("guess the number : "))
    if guess < secret_number:
        print(" too low number  ")
    elif guess > secret_number:
        print("too high")
    else:
        print("congratualitions! you have guessed it correct")

