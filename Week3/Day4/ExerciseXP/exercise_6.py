# 🌟 Exercise 6: Birthday and minutes
# Key Python Topics:

# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method

# Instructions:
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

from datetime import datetime

def hours_since_birth(date_of_birth: str) -> None:
    birth = datetime.strptime(date_of_birth, "%d/%m/%Y")
    now = datetime.now()
    print(f"minutes since birth: {int((now - birth).total_seconds()//60)} minutes")

hours_since_birth("1/1/2020")
