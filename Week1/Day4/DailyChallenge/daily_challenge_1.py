# Challenge 1: Multiples of a Number


# Key Python Topics:
# input() function
# Loops (for or while)
# Lists and appending items
# Basic arithmetic (multiplication)


# Instructions:
# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

# Example 1:

# Input:

# number: 7
# length: 5
# Output:
# [7, 14, 21, 28, 35]



# Example 2:

# Input:

# number: 12
# length: 10
# Output:
# [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]



# Example 3:

# Input:

# number: 17
# length: 6
# Output:
# [17, 34, 51, 68, 85, 102]

user_number = int(input("Enter a number (positive integer): "))
user_length = int(input("Enter the length of the list: "))

multiples_list = [n * user_number for n in range(1, user_length + 1)]

print(multiples_list)