# 🌟 Exercise 1: Random Sentence Generator
# Goal: Create a program that generates a random sentence of a specified length from a word list.

# Key Python Topics:
# File handling (open(), read())
# Lists
# Random number generation (random.choice())
# String manipulation (split(), join(), lower())
# Error handling (try, except)
# Input validation

# Instructions:
# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.

# Step 1: Create the get_words_from_file function
# Create a function named get_words_from_file that takes the file path as an argument.
# Open the file in read mode ("r").
# Read the file content.
# Split the content into a list of words.
# Return the list of words.

# Step 2: Create the get_random_sentence function
# Create a function named get_random_sentence that takes the sentence length as an argument.
# Call get_words_from_file to get the list of words.
# Select a random word from the list length times.
# Create a sentence with the selected words.
# Convert the sentence to lowercase.
# Return the sentence.

# Step 3: Create the main function
# Create a function named main.
# Print a message explaining the program’s purpose.
# Ask the user for the desired sentence length.
# Validate the user input:
# Check if it is an integer.
# Check if it is between 2 and 20 (inclusive).
# If the input is invalid, print an error message and exit.
# If the input is valid, call get_random_sentence with the length and print the generated sentence.
from random import choices

def get_words_from_file(file_path: str) -> list[str]:
    """
    generates a list of all words in a txt file
    
    :param file_path: path to the txt file
    :type file_path: str
    :return: list with words in the txt file
    :rtype: list[str]
    """
    with open(file_path, "r") as f:
        word_list = f.read().split()
        return word_list

def get_random_sentence(length: int) -> str:
    """
    creates a sentence with length random words from word_list
    
    :param length: number of words in the sentence
    :type length: int
    :return: a randomly-generated sentence with length words 
    :rtype: str
    """
    word_list = get_words_from_file("Week3/Day5/ExerciseXP/words.txt")
    words_for_sentence = choices(word_list, k = int(length))
    random_sentence = (" ".join(words_for_sentence)).lower() + "."
    return random_sentence

def main():
    print("This program generates a random sentence of a specified length from a word list.")
    print()
    length = input("Enter the number of words of the random sentence: ")

    if length.isdigit() and 2 <= int(length) <= 20:
        print()
        print(get_random_sentence(int(length)))
    else:
        print("invalid input.")

main()

# 🌟 Exercise 2: Working with JSON
# Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.

# Key Python Topics:
# JSON parsing (json.loads())
# JSON serialization (json.dump())
# Dictionaries
# File handling (open())

# Instructions:
# Using the follow code:
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"

# Access the nested “salary” key.
# Add a new key “birth_date” wich value is of format “YYYY-MM-DD”, to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Save the modified JSON to a file.

# Step 1: Load the JSON string
# Import the json module.
# Use json.loads() to parse the JSON string into a Python dictionary.

# Step 2: Access the nested “salary” key
# Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
# Print the value of the “salary” key.

# Step 3: Add the “birth_date” key
# Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Replace "YYYY-MM-DD" with an actual date.

# Step 4: Save the JSON to a file
# Open a file in write mode ("w").
# Use json.dump() to write the modified dictionary to the file in JSON format.
# Use the indent parameter to make the JSON file more readable.

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

business = json.loads(sampleJson)
print(f"Emma's salary: {business["company"]["employee"]["payable"]["salary"]}")
business["company"]["employee"]["birth_date"] = "1989-12-12"

with open('Week3/Day5/ExerciseXP/data.json', 'w') as d:
    json.dump(business, d, indent=2)