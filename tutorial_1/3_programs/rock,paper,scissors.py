import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? ").lower()

    if player == computer:
        print("computer: {}".format(computer))
        print("Player: {}".format(player))
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: {}".format(computer))
            print("Player: {}".format(player))
            print("You lose!")
        if computer == "scissors":
            print("computer: {}".format(computer))
            print("Player: {}".format(player))
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: {}".format(computer))
            print("Player: {}".format(player))
            print("You lose!")
        if computer == "paper":
            print("computer: {}".format(computer))
            print("Player: {}".format(player))
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: {}".format(computer))
            print("Player: {}".format(player))
            print("You lose!")
        if computer == "rock":
            print("computer: {}".format(computer))
            print("Player: {}".format(player))
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")

# choices = ("rock", "paper", "scissors")
# lostMap = {
#     "rock": "paper",
#     "paper": "scissors",
#     "scissors": "rock",
# }


# while True:
#     player = None
#     computer = random.choice(choices)

#     while player not in choices:
#         if player != None:
#             print('You choice must be rock, paper or scissors!')
#         player = input("rock, paper, or scissors? ").lower()

#     print("computer: ", computer)
#     print("You: ", player)

#     if player == computer:
#         print("Tie!")
#     elif player == lostMap[computer]:
#         print("You win!")
#     else:
#         print("You lose")

#     play_again = None
#     while play_again not in ["yes", "no"]:
#         play_again = input("Play again?(yes / no) ").lower()

#     if play_again == "no":
#         break
