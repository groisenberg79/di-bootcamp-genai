# Instructions: Old MacDonald’s Farm

# You are given example code and output. Your task is to create a Farm class that produces the same output.


# Step 1: Create the Farm Class
# Create a class called Farm.
# This class will represent a farm and its animals.

# Step 2: Implement the __init__ Method
# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes: name to store the farm’s name and animals to store the animals (initialize as an empty dictionary).


# Step 3: Implement the add_animal Method
# Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

# Step 4: Implement the get_info Method
# Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.

# Step 5: Test Your Code
# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.

# Example:
# class Farm:
#     def __init__(self, farm_name):
#         # ... code to initialize name and animals attributes ...

#     def add_animal(self, animal_type, count):
#         # ... code to add or update animal count in animals dictionary ...

#     def get_info(self):
#         # ... code to format animal info from animals dictionary ...

# # Test the code 
# macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# #output:
# # McDonald's farm

# # cow : 5
# # sheep : 2
# # goat : 12

# #     E-I-E-I-0!

# Bonus: Expand The Farm

# Step 6: Implement the get_animal_types Method
# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
# Use the sorted() function to sort the list.

# Step 7: Implement the get_short_info Method
# Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name if its count is greater than 1.
# Use string formatting to create the output.

# Step 8: upgrade the add_animal Method
# use **kwargs for passing multiple animals. The keys will be the animal name and the value will be the quantity.
# Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)

FARM_MESSAGE = "E-I-E-I-0!"

class Farm:
    """
    A class used to represent a farm

    Attributes
    ----------

    name: str
        name of the farm

    animals: dict
        a dict with 
            - key => name of animal
            - value => number of <key>s

    Methods
    -------

    add_animal(**kwargs)
        Adds each animal:count pair to the animal dictionary (if the animal is not in the dictionary)
        Updates the <animal> value if it already is in the dictionary adding the <count> to the <animal> value
    
    get_info()
        Returns a string that displays the farm's name, the animals and their counts,
        and the “E-I-E-I-0!” phrase

    add_number_morphology(animal)
        Adds number morphology to get_short_info() animals

    get_short_info()
        Returns the short string '[farm's name]'s farm has [names of each animal]' 

    get_animal_types()
        Returns a sorted list of all animal types (keys from the animals dictionary)
    

    """
    def __init__(self, farm_name: str):
        self.name = farm_name
        self.animals = dict()

    def add_number_morphology(self, animal: str) -> str:
        """
        Adds number morphology to get_short_info() animals
        
        :param animal: the animal whose morphology has to be updated
        :type animal: str
        :return: the animal string updated for number morphology
        :rtype: str
        """
        if self.animals[animal] > 1:
            return f"{animal}s"
        else:
            return f"a {animal}"

    def add_animal(self, **kwargs) -> None:
        """
        Adds each animal:count pair to the animal dictionary (if the animal is not in the dictionary)

        Updates the animal count value if it already is in the dictionary adding the count to the animal value
        
        :param kwargs: animal=count pairs where

            - animal => the animal's name

            - count => the amount of animal
        """
        for animal, count in kwargs.items():
            self.animals[animal] = self.animals.get(animal, 0) + count

    def get_info(self) -> str:
        """
        Returns a string that displays the farm's name, the animals and their counts,
        and the “E-I-E-I-0!” phrase
        
        :return: string with farm's name, animal count and “E-I-E-I-0!” phrase
        :rtype: str
        """
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            info += f"\n{animal:<8} : {count:>3}"
        info += f"\n\n{FARM_MESSAGE:^20}"
        return info

    def get_animal_types(self) -> list:
        """
        Returns a sorted list of all animal types (keys from the animals dictionary)
        
        :return: sorted list of animal types
        :rtype: list
        """
        return sorted(list(self.animals.keys()))
    
    def get_short_info(self) -> str:
        """
        Returns the short string '[farm's name]'s farm has [names of each animal]' 
        
        :return: string with short description of the farm
        :rtype: str
        """
        animals_list = self.get_animal_types()
        short_info = f"{self.name}'s farm has " 
        for index, animal in enumerate(animals_list):
            if len(animals_list) == 1:
                short_info += f"{self.add_number_morphology(animal)}."
            elif index < len(animals_list) - 1: # if it is not the last animal in the list
                short_info += f"{self.add_number_morphology(animal)}, "
            else: # it is the last animal of a list with more than one animal
                short_info += f"and {self.add_number_morphology(animal)}."
        return short_info
    
macdonald = Farm("McDonald")
macdonald.add_animal(cow = 5, sheep = 2, goat = 12)
print(macdonald.get_info())
print(macdonald.get_short_info())