# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)

# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {1, 2, 4, 6}
print(f"initial my_fav_numbers: {my_fav_numbers}")

my_fav_numbers.update([2.71, 3.14])
print(f"my_fav_numbers after adding two numbers: {my_fav_numbers}")

friend_fav_numbers = {4, 5, 6, 7, 8, 9, 10}
print(f"friend_fav_numbers: {friend_fav_numbers}")

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("------------------------------------------")

print(f"my_fav_numbers final: {my_fav_numbers}")
print(f"friend_fav_numbers final: {friend_fav_numbers}")
print(f"union of my_fav_numbers and friend_fav_numbers: {our_fav_numbers}")

# 🌟 Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)


# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

my_tuple = (1,2, 3)
print(f"initial tuple: {my_tuple}")

my_tuple += (4, 5, 6)
print(f"final tuple: {my_tuple}")

# 🌟 Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear


# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

num_apples = basket.count("Apples")
print(f"number of apples: {num_apples}")

print(f"fruit basket in initial state: {basket}")

basket.clear()
print(f"fruit basket final state: {basket}")

# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

# What is a float?
# Answer:   A float (short for floating-point number) in Python is a data type 
#           used to represent real numbers that have a fractional, or decimal, component.
#           Floats are defined by the presence of a decimal point (e.g., 3.14) or
#           by the use of the scientific notation (e.g., 2e2, which is 200.0)

# What’s the difference between a float and an integer?
# Answer:   integers are used to represent whole numbers, 
#           while floats are used to represent real numbers with fractional components.
#           Formally, integers are numbers without a decimal point, while 
#           floats either have decimal points or use scientific notation.

number_list = []
for i in range(1, 6):
    number_list.append(i)
    if i < 5:
        number_list.append(i + 0.5)

print(number_list)

# 🌟 Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 🌟 Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

user_name = input("Enter your name: ")
while True:
    if user_name.isdigit() or len(user_name) < 3:
        user_name = input("Give the correct name: ")
        continue
    else:
        print("Thank you.")
        break

# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

user_fav_fruits = input("Enter your favorite fruits (type each fruit and separate it by a space):").lower()
fav_fruits_list = user_fav_fruits.split()

user_fruit = input("Enter the name of a fruit: ").lower()
if user_fruit in fav_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings_list = []

while True:
    topping = input("Enter a topping: ").lower()
    if topping == "quit":
        break
    else:
        toppings_list.append(topping)

print("Your toppings:")
for topp in toppings_list:
    print(topp)
print(f"You have to pay: ${10 + len(toppings_list)*2.50}")

# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

ages = input("Enter the age of each person separated by space: ")
age_list = ages.split()

age_list = [int(x) for x in age_list]

ticket_cost = 0
for age in age_list:
    if 3 <= age <= 12:
        ticket_cost += 10
    elif age > 12:
        ticket_cost += 15

print(f"The total ticket cost is ${ticket_cost}.")