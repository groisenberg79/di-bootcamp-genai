# Instructions
# Create a new directory for the game. Inside it, create 2 files:
# rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.
# game.py – this will contain a Game class which will have functions to play a single game of rock-paper-scissors against the computer, determine the game’s result, and return the result.

# Steps

# Part I - game.py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# (1) Get the user’s item (rock/paper/scissors) and remember it
# (2) Get a random item for the computer (rock/paper/scissors) and remember it
# (3) Determine the results of the game by comparing the user’s item and the computer’s item:
#   (a) **Print** the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

#   (b) **Return** the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# Part II - rock-paper-scissors.py

# rock-paper-scissors.py : create 3 functions

# get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
# The possibles choices are : Play a new game or Show scores or Quit

# print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.
# *Note*: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.

# main() - the main function. It should take care of 3 things:

# (1) Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)

# (2) When the user chooses to play a game:
# - Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
# - Remember the results of every game that is played.

# (3) When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.
from __future__ import annotations
from random import choice

GAME_CHOICES = ["r", "p", "s"] # the only choices permitted in the main menu

class Game:
    def get_user_item(self) -> str:
        """
        Asks the user to select an item (rock/paper/scissors) and
        returnsn the item selected
        
        :return: the user selection
        :rtype: str
        """
        while True:
            # keeps asking the user for an item until item is valid
            user_item = input("Select (r)ock, (p)apers or (s)cissors: ").lower().strip()
            if user_item not in GAME_CHOICES:
                print("Invalid choice.")
                print()
                continue
            return user_item
    
    def get_computer_item(self) -> str:
        """
        Gets random computer choice

        :return: the random computer choice
        :rtype: str
        """
        return choice(GAME_CHOICES)
    
    def get_game_result(self, user_item: str, computer_item: str) -> str:
        """
        Determines the result of the game.

        :param user_item: the item chosen by the user
        :type user_item: str
        :param computer_item: the item chosen by the computer
        :type computer_item: str
        :return: the result ("win", "loss" or "draw")
        :rtype: str
        """
        if (user_item == "s" and computer_item == "p" or
            user_item == "p" and computer_item == "r" or
            user_item == "r" and computer_item == "s"):
            return "win"
        elif user_item == computer_item:
            return "draw"
        return "loss"
    
    def play(self) -> str:
        """
        Plays a single round of the game

        :return: the result of the game round
        :rtype: str
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selected: {user_item}. The computer selected: {computer_item}.")
        print(f"Result: {result}.")
        print()
        return result