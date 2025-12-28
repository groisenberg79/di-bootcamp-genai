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

sparkles = Cat("Sparkles", 5)
bob = Cat("Bob", 12)
lymphoma = Cat("Lymphoma", 3)

oldest_cat = find_oldest_cat(sparkles, bob, lymphoma)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# 🌟 Exercise 2 : Dogs
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)

# Instructions:
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

# Step 4: Compare Dog Sizes

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("Lily", 30)
sarahs_dog = Dog("Alberto", 45)

davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is higher than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} is higher than {sarahs_dog.name}")

# 🌟 Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists

# Instructions:
# Create a Song class with a method to print song lyrics line by line.

# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

# Example:
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

class Song:
    """
    A class used to represent song lyrics

    Attributes
    ----------
    lyrics: list
    - a list whose items are the verses of a song (strings)

    Methods
    -------
    sing_me_a_song()
        Prints the verses of the song

    """
    def __init__(self, lyrics):
        """
        :param lyrics: a list whose elements are the verses (strings) of the song
        :type lyrics: list
        """
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        """
        Prints the verses of the song
        """
        for verse in self.lyrics:
            print(verse)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# 🌟 Exercise 4 : Afternoon at the Zoo

# Goal:
# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists
# Dictionaries (for grouping)
# String manipulation

# Instructions

# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.

# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.

# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.

# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.

# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.

# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
# Example output:
# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }

# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().
# Example output:
# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...

# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.
# Example (No Internal Logic Provided)
# class Zoo:
#     def __init__(self, zoo_name):
#         pass

#     def add_animal(self, new_animal):
#         pass

#     def get_animals(self):
#         pass

#     def sell_animal(self, animal_sold):
#         pass

#     def sort_animals(self):
#         pass

#     def get_groups(self):
#         pass

# # Step 2: Create a Zoo instance
# brooklyn_safari = Zoo("Brooklyn Safari")

# # Step 3: Use the Zoo methods
# brooklyn_safari.add_animal("Giraffe")
# brooklyn_safari.add_animal("Bear")
# brooklyn_safari.add_animal("Baboon")
# brooklyn_safari.get_animals()
# brooklyn_safari.sell_animal("Bear")
# brooklyn_safari.get_animals()
# brooklyn_safari.sort_animals()
# brooklyn_safari.get_groups()


# Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time for a new animal, you can pass multiple animals names separated by a comma.

class Zoo:
    """A class used to represent a Zoo and its animals
    
    Attributtes
    -----------
    zoo_name: str
        - name of the zoo
    animals: list
        - list of all animals in the zoo
    animals_dict: dict
        - dictionary with 
            key = letter of the alphabet
            value = sorted list of all animals whose first letter is <key>

    Methods
    -------
    add_animal(*new_animals)
        Adds animals to the list of zoo animals.
    get_animals()
        Prints all the animals currently in the zoo.
    sell_animal(animal_sold)
        If animal_sold is on the list of animals, remove it from the list.
    sort_animals()
        Creates a key-sorted dict where each key is a letter and
        each value is a sorted list of animals whose first letter is <key>.
    get_groups()
        Prints the grouped animals as created by sort_animals()
            """

    def __init__(self, zoo_name: str) -> None:
        """        
        :param zoo_name: the zoo's name
        :type zoo_name: str
        """
        self.zoo_name = zoo_name
        self.animals = list()

    def add_animal(self, *new_animals: str) -> None:
        """
        Adds animals to the list of zoo animals.

        If animal is already in the list, prints a message informing the user. 
               
        :param new_animals: one or more string objects representing animals
        :type new_animals: str
        """
        for animal in new_animals:
            if animal not in self.animals:  # if animal is new, append it to the list
                self.animals.append(animal)
            else:
                print(f"{animal} already in the zoo.")

    def get_animals(self) -> None:
        """
        Prints all the animals currently in the zoo.
        """
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold: str) -> None:
        """
        If animal_sold is on the list of animals, remove it from the list.
        
        :param animal_sold: animal that will be removed from animals list
        :type animal_sold: str
        """
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self) -> dict:
        """
        Creates a key-sorted dictionary where each key is a letter and

        each value is a sorted list of animals whose first letter is <key>.
        
        :return: dictionary with letters as keys and sorted lists of animals as values
        :rtype: dict
        """
        animal_dict = dict()
        for animal in self.animals:
            if animal[0] not in animal_dict.keys(): # if the first letter of animal is not a key
                animal_dict[animal[0]] = [animal]   # add the key and the corresponding value,
                                                    # which is a list whose only value is animal
            else:
                animal_dict[animal[0]].append(animal)   # if there is already a key, append animal
                                                        # to the list (the value of the key)
        for key, value in animal_dict.items():
            animal_dict[key] = sorted(value)    # sort the value of each key
        return dict(sorted(animal_dict.items()))   # return a dict sorted by key 

    
    def get_groups(self) -> None:
        """
        Prints the grouped animals as created by sort_animals()
        """
        animals_dict = self.sort_animals()
        for key in animals_dict.keys():
            print(f"{key}: {animals_dict[key]}")

brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Wolf", "Giraffe", "Bear", "Baboon", "Whale")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
