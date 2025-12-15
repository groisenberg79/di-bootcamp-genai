# Exercise 1: Hello World
# Instructions
# Print the following output using one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

greeting = "Hello world"

for i in range(4):
    print(greeting)

# Exercise 2: Some Math
# Instructions
# Write code that calculates the result of:

# (99^3)*8 (meaning 99 to the power of 3, times 8).

calculation = (99**3)*8

print(calculation)

# Exercise 3: What is the output?
# Instructions
# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare
# Example:
# >>> 15 < 8 #False


# >>> 5 < 3 #False
# >>> 3 == 3 #True
# >>> 3 == "3" #False
# >>> "3" > 3 #TypeError
# >>> "Hello" == "hello" #False

# 🌟 Exercise 4: Your computer brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = "Mac"

print(f"I have a {computer_brand} computer.")

# 🌟 Exercise 5: Your information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = "Gabriel"
age = 46
shoe_size = 43
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."

print(info)

# 🌟 Exercise 6: A & B
# Instructions
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = 8
b = 7

if a > b:
    print("Hello World")

# Exercise 7: Odd or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

user_number = int(input("Enter a positive integer: "))

if user_number % 2 == 0:
    print(f"{user_number} is an even number.")
else:
    print(f"{user_number} us an odd number.")

# 🌟 Exercise 8: What’s your name?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

user_name = input("Enter your name: ").capitalize()

if user_name == "Gabriel":
    print("We have the same name! Awesome!")
else:
    print("We don't have the same name. What a bummer.")

# 🌟 Exercise 9: Tall enough to ride a roller coaster
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

user_height = int(input("Enter your height (in centimeters): "))

if user_height > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")

