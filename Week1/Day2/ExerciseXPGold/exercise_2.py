# Exercise 2 : What is the Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = int(input("Enter a month (an integer between 1 and 12): "))

if 3 <= month <= 5:
    season = "Spring"
elif 6 <= month <= 8:
    season = "Summer"
elif 9 <= month <= 11:
    season = "Autumn"
else:
    season = "Winter"

print(f"This month is in the {season}.")