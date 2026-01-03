# 🌟 Exercise 4: Family and Person Classes
# Goal:
# Practice working with classes and object interactions by modeling a family and its members.

# Key Python Topics:
# Classes and objects
# Instance methods
# Object interaction
# Lists and loops
# Conditional statements (if/else)
# String formatting (f-strings)

# Instructions:

# Step 1: Create the Person Class
# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.

# Step 2: Create the Family Class
# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)

# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.

# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."

# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.

# Expected Behavior:
# Once implemented, your program should allow you to:
# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output.

class Person:
    def __init__(self, first_name: str, age: int, last_name: str = ""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False

class Family:
    def __init__(self, last_name: str, members: list = []):
        self.last_name = last_name
        self.members = members

    def born(self, first_name: str, age: int) -> bool:
        self.members.append(Person(first_name, age, self.last_name))

    def check_majority(self, first_name: str):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                break

    def family_presentation(self):
        print(f"Family's name: {self.last_name}")
        for person in self.members:
            print(f"first name: {person.first_name}, age: {person.age}")

the_mccarthys = Family("McCarthy")

the_mccarthys.born("Bill", 18)
the_mccarthys.born("John", 34)
the_mccarthys.born("Mary", 6)
the_mccarthys.born("Sofia", 76)

print("Can Bill get out?")
the_mccarthys.check_majority("Bill")
print()
print("Can Mary get out?")
the_mccarthys.check_majority("Mary")

the_mccarthys.family_presentation()