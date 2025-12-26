# What you will create
# Use python to create a Hangman game.

# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
body_parts = ["O", "/", "|", "\\", "/", "\\"]
player_body = ["", "", "", "", "", ""]
guessed_letters = list()
wrong_guesses = list()

def display_scaffold(player_body: list) -> None:
    """Display the current scaffold"""
    print(" _________")
    print(" |       |")
    print(" |       |")
    print(f" |       {player_body[0]}")
    print(f" |      {player_body[1]}{player_body[2]}{player_body[3]}")
    print(f" |      {player_body[4]} {player_body[5]}")
    print(" |")
    print(" ----------")

def update_guessed_letters(word: str, player_guess: str, guessed_letters: list) -> None:
    """If the player guesses a correct letter,\n
    update the guessed letters list with the guessed letter"""
    for index, letter in enumerate(word):
        if player_guess == letter:
            guessed_letters[index] = letter

def update_player_body(player_body: list) -> None:
    """if the player guesses a wrong letter,\n
    update the gallows with new body part"""
    for index, body_part in enumerate(player_body):
        if body_part == "":
            player_body[index] = body_parts[index]
            break

def make_guess(word: str, guessed_letters: list) -> None:
    """Take a guess from the player and\n
    update the guessed letters list or update the player's body"""
    player_guess = input("Enter a letter: ")
    if player_guess in word:
        if player_guess not in guessed_letters:
            print("Correct guess!")
            update_guessed_letters(word, player_guess, guessed_letters)
        else:
            print("This letter was already guessed.")
            make_guess(word, guessed_letters)
    else:
        print("Wrong guess!")
        update_player_body(player_body)
        wrong_guesses.append(player_guess)
        print("Your wrong guesses so far: ", " ".join(wrong_guesses))

def has_player_lost(player_body: list) -> bool:
    """check if the player has lost;\n
    if that's the case, returns True, otherwise False"""
    if all(body_part != "" for body_part in player_body):
        return True
    else:
        return False
    
def create_guessed_letters(word: str) -> list:
    """declare a guessed letters list"""
    guessed_letters = ["*" for index in range(len(word))]
    return guessed_letters

def display_guessed_letters(guessed_letters: list) -> None:
    """display the partially guessed word,\n
    with the non-guessed letters substituted by stars (*)"""
    print("Secret word: ", end="")
    for letter in guessed_letters:
        print(letter, end=" ")
    print()

def play():
    word = random.choice(wordslist)
    print("Welcome to Hangman!")
    guessed_letters = create_guessed_letters(word)
    while not has_player_lost(player_body):
        display_scaffold(player_body)
        display_guessed_letters(guessed_letters)
        make_guess(word, guessed_letters)
        if has_player_lost(player_body):
            print(f"You lost! The secret word was {word}!")
            break
        elif "".join(guessed_letters) == word:
            print(f"You won! The secret word was {word}")
            break

play()
