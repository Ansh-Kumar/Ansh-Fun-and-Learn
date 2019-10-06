import random

choices = ["rock", "paper", "scissors"]
print("Rock crushes scissors. Scissors cuts paper. Paper covers Rock.")
player = input("Do you want to be rock paper or scissors (or quit)?     ")
while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("You chose " +player+ ", and the computer chose " +computer+  ".")
    if player == computer:
        print("It is a tie")
    elif player == "rock":
        if computer == "scissors":
            print("You win")
        else:
            print("You lose")
    elif player == "paper":
        if computer == "rock":
            print("You win")
        else:
            print("You lose")
    elif player == "scissors":
        if computer == "paper":
            print("You win")
        else:
            print("You lose")
    else:
        print("I think there was an error...")
    print()                 #Skip a line
    player = input("Do you want to be rock paper or scissors (or quit)?     ")
