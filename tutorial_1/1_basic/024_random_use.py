import random

# generate a random number between one and six
x = random.randint(1, 6)
print(x)

# generate a random number between zero and one
y = random.random()
print(y)

# Choose a random element from a non-empty sequence.
myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print(z)

# shuffle the list
cards = [1, 2, 3, 4, 5, 6, 7, "J", "Q", "K", "A"]
random.shuffle(cards)

print(cards)
