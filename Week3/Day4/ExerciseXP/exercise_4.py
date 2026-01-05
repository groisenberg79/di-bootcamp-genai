# 🌟 Exercise 4: Current Date
# Goal: Create a function that displays the current date.

# Key Python Topics:
# datetime module

# Instructions:
# Use the datetime module to create a function that displays the current date.

# Step 1: Import the datetime module

# Step 2: Get the current date

# Step 3: Display the date

import datetime

current_date = datetime.date.today()

print(f"Today is the {current_date.strftime("%d/%m/%y")}")