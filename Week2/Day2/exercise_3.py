# 🌟 Exercise 3: Some Geography
# Goal: Create a function that describes a city and its country.

# Key Python Topics:
# Functions with multiple parameters
# Default parameter values
# String formatting

# Step 1: Define a Function with Parameters ok

# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.

# Step 2: Print a Message

# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.

# Step 3: Call the Function

# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").

# Expected Output:
# Reykjavik is in Iceland.
# Paris is in Unknown.

def describe_city(city: str, country: str ='Unknown') -> None:
    """This functions takes two args (a city and a country)\n
    and prints that the given city is in the given country"""
    print(f"{city} is in {country}.")

def main():
    describe_city("Reykjavik", "Iceland")
    describe_city("Paris")

main()
