import random

options = ("rock", "paper", "scissors")

player = None

while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ").strip().lower()

computer = random.choice(options)

if player == computer:
    print("The game is a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
else:
    print("You lose!")

print(f"Player: {player}")
print(f"Computer: {computer}")
