# Challenge 1: Sorting

# Instructions:
# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.

# Step 1: Get Input
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.

# Step 2: Split the String

# Step 3: Sort the List

# Step 4: Join the Sorted List

# Step 5: Print the Result

# Print the resulting comma-separated string.

# Expected Output:

# If the input is without,hello,bag,world, the output should be bag,hello,without,world.

user_input = input("Enter words separated by commas: ")

words_list = user_input.split(",")
words_sorted = sorted(words_list)
new_string = ",".join(words_sorted)

print(new_string)



