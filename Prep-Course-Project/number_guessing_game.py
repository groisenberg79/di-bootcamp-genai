""" Build a fun Number Guessing Game in Python! 🐍 The program picks a random number between 1-100, and you have 7 attempts to guess it. Get hints if you’re too high 📈 or too low 📉! Perfect for practicing loops 🔄, conditionals ❓, and user input ⌨️.
 """

import random

print("Welcome to the 'Guess the Number' Game!")
print()

print("This is how the game works: \n"
    "- I will pick a random integer between 1 and 100 and you have to guess which number it is.\n"
    "- Each time you pick a wrong guess, I will give you hints (whether is is higher or lower).\n"
    "- You will have 7 attempts until the game ends (and you lose).\n"
    "- Find the number in any of the 7 attempts, and you win!\n")

random_int = random.randint(1, 100)    # select a random integer
correct_guess = False                   # track if guess is correct

for attempt in range(7):
    attempt +=1
    guess = int(input("Guess an integer betweeen 1 and 100: "))
    if guess == random_int:
        correct_guess = True
        break
    elif guess < random_int:
        print("\nYour guess is too low!\n")
    elif guess > random_int:
        print("\nYour guess is too high!\n")
    print(f"You have {7 - attempt} attempts left.\n")

if correct_guess == True:
    print("Congratulations -- your guess was correct!\n")
else:
    print("You ran out of attempts -- you lost the game!\n")
print(f"The secret integer was {random_int}.")

