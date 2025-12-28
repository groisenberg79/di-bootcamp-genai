# 🌟 Exercise 1: Cats

# Key Python Topics:
# Classes and objects
# Object instantiation
# Attributes
# Functions

# Instructions:
# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

# Step 1: Create Cat Objects
# Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat
# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

# Step 3: Print the Oldest Cat’s Details
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

# Example:
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# # Step 1: Create cat objects
# # cat1 = create the object

# # Step 2: Create a function to find the oldest cat
# def find_oldest_cat(cat1, cat2, cat3):
#     # ... code to find and return the oldest cat ...

# # Step 3: Print the oldest cat's details

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = cat1
    for cat in [cat1, cat2, cat3]:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

def main():
    sparkles = Cat("Sparkles", 5)
    bob = Cat("Bob", 12)
    lymphoma = Cat("Lymphoma", 3)

    oldest_cat = find_oldest_cat(sparkles, bob, lymphoma)

    print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

main()