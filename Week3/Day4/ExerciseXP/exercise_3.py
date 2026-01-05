# 🌟 Exercise 3: String module

# Goal: Generate a random string of length 5 using the string module.

# Instructions:
# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.

# Key Python Topics:
# string module
# random module
# String concatenation

# Step 1: Import the string and random modules
# Import the string and random modules.

# Step 2: Create a string of all letters
# Read about the strings methods HERE to find the best methods for this step

# Step 3: Generate a random string
# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.

import string, random

all_letters = string.ascii_letters
chosen_letters = list()

for index in range(5):
    chosen_letters.append(random.choice(all_letters))

final_string = "".join(chosen_letters)
print(final_string)