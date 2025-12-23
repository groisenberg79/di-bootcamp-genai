# 🌟 Exercise 6: Magicians…
# Goal: Modify a list of magician names and display them in different ways.

# Key Python Topics:
# Lists
# for loops
# Modifying lists
# Functions that modify data structures

# Step 1: Create a List of Magician Names
# Create a list called magician_names with the given names:
# ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Step 2: Create a Function to Display Magicians
# Create a function called show_magicians() that takes the magician_names list as a parameter.
# Inside the function, iterate through the list and print each magician’s name.

# Step 3: Create a Function to Modify the List
# Create a function called make_great() that takes the magician_names list as a parameter.
# Inside the function, use a for loop to iterate through the list and add “the Great” before each magician’s name.

# Step 4: Call the Functions
# Call make_great() to modify the list.
# Call show_magicians() to display the modified list.

# Expected Output:
# Harry Houdini the Great
# David Blaine the Great
# Criss Angel the Great

def show_magicians(magician_names: list) -> None:
    """This function takes a list of magician names\n
    and prints their names"""
    for magician in magician_names:
        print(magician)

def make_great(magician_names: list) -> None:
    """This function takes a list of magician names\n
    and add 'the Great' to the end of their names"""
    for index, magician in enumerate(magician_names):
        magician_names[index] = magician + " the Great"
        
def main():
    magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    make_great(magician_names)
    show_magicians(magician_names)

main()
