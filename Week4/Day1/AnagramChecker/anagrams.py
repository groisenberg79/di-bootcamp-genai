from anagram_checker import AnagramChecker

USER_OPTIONS = {'w', 'x'}

def get_user_menu_choice() -> str:
    """
    gets the user choice (if he wants anagrams for a word or exit)
    
    :return: the user choice
    :rtype: str
    """
    while True:
        user_choice = input("Press w to enter a word or x to exit: ").lower().strip()
        if user_choice in USER_OPTIONS:     # is a valid choice
            return user_choice
        print("Invalid input.")

def get_user_word() -> str:
    """
    Gets the word chosen by the user to obtain anagrams
    
    :return: the chosen by the user
    :rtype: str
    """
    while True:
        user_word = input("Enter a valid word: ").strip().upper()
        if user_word == "":
            print("only non-empty input allowed.")
        elif " " in user_word:          # if there is more than one word
            print("only one word allowed.")
        elif not user_word.isalpha():   # if there are non-alphabetic characters
            print("no numbers or special characters allowed.")
        else:
            return user_word
    
def print_anagrams(anagrams: list[str]) -> None:
    """
    Prints all anagrams (if any) for a given word
    
    :param anagrams: the list of all anagrams of a given word
    :type anagrams: list[str]
    """
    if anagrams == []:
        print("This word has no anagrams.")
    else:
        print("Anagrams for your word: ", end="")
        for index, word in enumerate(anagrams):
            if index == len(anagrams) - 1:
                print(word)
            else:
                print(word, end=", ")

def begin_anagram_generation():
    """
    Starts the process of anagram generation
    """
    checker = AnagramChecker()
    while True:
        user_word = get_user_word()
        if checker.is_valid_word(user_word):            # if the word is a valid word
            anagrams = checker.get_anagrams(user_word)  # collects all anagrans
            print(f"Your word: \"{user_word.upper()}\"")
            print("This is a valid English word.")
            print_anagrams(anagrams)                    # print the anagrams
            print()
            break
        print("not a valid word.")

def execute_user_choice(user_choice: str):
    """
    Proceeds to execute the user choice from the main menu (get anagrams or exit)
    
    :param user_choice: the user choice ('w' or 'x')
    :type user_choice: str
    """
    while True:
        if user_choice == "w":
            begin_anagram_generation()
            user_choice = get_user_menu_choice() # calls main menu after finding anagrams
        else:
            print("Thanks for using Anagram Finder©!")
            break

def main():
    print("Welcome to Anagram Finder©!")
    print()
    user_choice = get_user_menu_choice()    # initial call of main menu
    execute_user_choice(user_choice)        # execution of first user choice from menu

main()
    
    






