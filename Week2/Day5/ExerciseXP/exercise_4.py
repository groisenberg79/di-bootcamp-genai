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

def main():
    brooklyn_safari = Zoo("Brooklyn Safari")
    brooklyn_safari.add_animal("Wolf", "Giraffe", "Bear", "Baboon", "Whale")
    brooklyn_safari.get_animals()
    brooklyn_safari.sell_animal("Bear")
    brooklyn_safari.get_animals()
    brooklyn_safari.sort_animals()
    brooklyn_safari.get_groups()

main()