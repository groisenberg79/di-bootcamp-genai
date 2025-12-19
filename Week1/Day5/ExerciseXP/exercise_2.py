# 🌟 Exercise 2: Cinemax #2
# Key Python Topics:

# Looping through dictionaries
# Conditionals
# Calculations


# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


# Family Data:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.


# Bonus:

# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

cost = 0 
for name in family.keys():
    if family[name] < 3:
        print(f"Ticket price for {name}: Free")
    elif 3 <= family[name] <= 12:
        cost += 10
        print(f"Ticket price for {name}: $10")
    else:
        cost += 15
        print(f"Ticket price for {name}: $15")
print()
print(f"The total cost is: ${cost}.")

