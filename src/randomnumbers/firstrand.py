import random

def flip_coin():
    result = random.choice(['Heads', 'Tails'])
    print(f"The coin landed on: {result}")

# Call the function to flip the coin
flip_coin()
