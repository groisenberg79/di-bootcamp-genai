# Instructions
# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

# import random
# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
# target_number   = 3728

# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

# For example
# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728

set_of_numbers = set(list_of_numbers)
list_of_numbers_no_repetitions = sorted(list(set_of_numbers))

last_index = len(list_of_numbers_no_repetitions) - 1

for index, number in enumerate(list_of_numbers_no_repetitions):
    for sub_index in range(index + 1, last_index + 1):
        if list_of_numbers_no_repetitions[index] + list_of_numbers_no_repetitions[sub_index] == target_number:
            print(f"{list_of_numbers_no_repetitions[index]} and {list_of_numbers_no_repetitions[sub_index]} sums to the target number {target_number}.")

