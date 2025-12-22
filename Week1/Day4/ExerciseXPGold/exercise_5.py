# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

def main():
    import string
    vowels = 'aeiou'
    alphabet_lowercase = string.ascii_lowercase

    for letter in alphabet_lowercase:
        if letter in vowels:
            print(f"{letter} is a vowel")
        else:
            print(f"{letter} is a consonant")

main()
