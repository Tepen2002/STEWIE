import random

number = random.randint(1, 10)
guess = input("Guess the number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("You won!")
else:
    print(f"Sorry, you lost. The correct number was {number}.")
