# Challenge 2: Remove Consecutive Duplicate Letters


# Key Python Topics:
# input() function
# Strings and string manipulation
# Loops (for or while)
# Conditional statements (if)


# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.



# Example 1:

# Input:
# user’s word: "ppoeemm"
# Output:
# "poem"


# Example 2:

# Input:
# user’s word: "wiiiinnnnd"
# Output:
# "wind"


# Example 3:

# Input:
# user’s word: "ttiiitllleeee"
# Output:
# "title"


# Example 4:

# Input:
# user’s word: "cccccaaarrrbbonnnnn"
# Output:
# "carbon"


# Notes:
# The final string will not include any consecutive duplicates, but non-consecutive duplicates are allowed.
# Example: In "recursive", the two ‘r’s and two ‘e’s are allowed because they are not consecutive.

user_word = input("Enter a word: ").lower()

new_word = str()

for i, letter in enumerate(user_word):
    if i == 0:
        new_word += letter
    elif letter != user_word[i - 1]:
        new_word += letter

print(new_word)
