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