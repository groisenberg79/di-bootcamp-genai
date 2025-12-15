# Exercise 7: Odd or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

user_number = int(input("Enter a positive integer: "))

if user_number % 2 == 0:
    print(f"{user_number} is an even number.")
else:
    print(f"{user_number} us an odd number.")