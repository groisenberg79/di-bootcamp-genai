# Exercise 9 : Random number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

def check_number(user_number, random_number):
    if user_number == random_number:
        print(f"Congratulations, you guessed the correct number: {random_number}")
    else:
        print(f"The correct number was {random_number}. Better luck next time!")

def main():
    import random
    random_number = random.randint(1, 9)
    user_number = int(input("Enter an integer between 1 and 9 (inclusive): "))
    check_number(user_number, random_number)

main()
