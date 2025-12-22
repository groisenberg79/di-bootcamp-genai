# Exercise 6: Words and letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
def search_char(user_char, words):
    for word in words:
        index = word.find(user_char)
        if index == -1:
            print(f"the word {word} does not have the letter {user_char}.")
        else:
            print(f"letter {user_char} found at index {index} in word {word}.")

def main():
    user_words = input("Enter seven words, separated by spaces: ").lower()
    words = user_words.split()
    user_char = input("Enter a single character: ").lower()

    search_char(user_char, words)

main()
    

        
