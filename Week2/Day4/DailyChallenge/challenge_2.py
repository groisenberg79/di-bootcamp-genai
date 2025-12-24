# Challenge 2: Longest Word

# Instructions:
# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.

# Step 1: Define the Function

# Define a function that takes a string (the sentence) as a parameter.

# Step 2: Split the Sentence into Words

# Step 3: Initialize Variables

# Step 4: Iterate Through the Words

# Step 5: Compare Word Lengths

# Step 6: Return the Longest Word
# Expected Output:
# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".

# Key Python Topics:
# Functions
# Strings
# .split() method
# Loops (for)
# Conditional statements (if)
# String length (len())

def longest_word(sentence: str) -> str:
    words_list = sentence.split(" ")
    longest = str()
    for index, word in enumerate(words_list):
        if index == 0:
            longest = word
        elif len(word) > len(longest):
                longest = word
    return longest

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))

        