import random
the_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 - 10:     "))
while guess != the_number:
    if guess > the_number:
        print("That is too high; try again.")
    if guess < the_number:
        print("That is too low; try again")
    guess = int(input("Guess again:     "))
print("That was correct. You are amazing")
