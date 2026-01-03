#  🌟 Exercise 1: Pets

# Key Python Topics:
# Inheritance
# Class instantiation
# Lists
# Polymorphism

# Instructions:
# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.

# Step 1: Create the Siamese Class
# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.

# Step 2: Create a List of Cat Instances
# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.

# Step 3: Create a Pets Instance
# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.

# Step 4: Take Cats for a Walk
# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.

# Example:
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# Step 1: Create the Siamese class

# Step 2: Create a list of cat instances

# Step 3: Create a Pets instance of the list of cat instances
# sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
# sara_pets.walk()

class Pets:
    def __init__(self, animals: list):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def walk(self) -> str:
        return f'{self.name} is just walking around'
    
class Siamese(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

class Bengal(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def sing(self, sounds) -> str:
        return f'{sounds}'

class Chartreux(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def sing(self, sounds) -> str:
        return f'{sounds}'

all_cats = [Bengal("Sparks", 10), Chartreux("Billy", 3), Siamese("Lulu", 7)]

sara_pets = Pets(all_cats)

sara_pets.walk()