# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings_list = []

while True:
    topping = input("Enter a topping: ").lower()
    if topping == "quit":
        break
    else:
        toppings_list.append(topping)

print("Your toppings:")
for topp in toppings_list:
    print(topp)
print(f"You have to pay: ${10 + len(toppings_list)*2.50}")