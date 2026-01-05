# 🌟 Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.

# Key Python Topics:
# datetime module
# Time difference calculations

# Instructions:
# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

# Step 2: Get the current date and time

# Step 3: Create a datetime object for January 1st of the next year

# Step 4: Calculate the time difference

# Step 5: Display the time difference

import datetime

today_datetime = datetime.datetime.now()

next_year_datetime = datetime.datetime(2027, 1, 1)

difference = next_year_datetime - today_datetime

print(f"time difference: {difference}")