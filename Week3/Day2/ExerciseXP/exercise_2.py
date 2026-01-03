# 🌟 Exercise 2: Dogs
# Goal: Create a Dog class with methods for barking, running speed, and fighting.

# Key Python Topics:
# Classes and objects
# Methods
# Attributes

# Instructions:

# Step 1: Create the Dog Class
# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “<dog_name> is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.

# Step 2: Create Dog Instances
# Create three instances of the Dog class with different names, ages, and weights.

# Step 3: Test Dog Methods
# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

# Example (Conceptual, No Direct Solution):
# class Dog:
#     def __init__(self, name, age, weight):
#         # ... code to initialize attributes ...

#     def bark(self):
#         # ... code to return bark message ...

#     def run_speed(self):
#         # ... code to return run speed ...

#     def fight(self, other_dog):
#         # ... code to determine and return winner ...

# # Step 2: Create dog instances
# #... your code here

# # Step 3: Test dog methods
# print(dog1.bark())
# print(dog2.run_speed())
# print(dog1.fight(dog2))

class Dog:
    def __init__(self, name: str, age: int, weight: int):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self) -> str:
        return f"{self.name} is barking."
    
    def run_speed(self) -> float:
        return self.weight/ self.age * 10
    
    def fight(self, other_dog: Dog) -> str:
        other_dog_speed = other_dog.run_speed()
        self_speed = self.run_speed()
        if other_dog_speed > self_speed:
            return f"{other_dog.name} won the fight!"
        elif self_speed > other_dog_speed:
            return f"{self.name} won the fight!"
        else:
            return "It's a draw!"

boris = Dog("Boris", 10, 30)
stevie = Dog("Stevie", 8, 20)
flavius = Dog("Flavius", 15, 12)

print(boris.bark())
print(stevie.run_speed())
print(flavius.fight(stevie))