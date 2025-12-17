# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {1, 2, 4, 6}
print(f"initial my_fav_numbers: {my_fav_numbers}")

my_fav_numbers.update([2.71, 3.14])
print(f"my_fav_numbers after adding two numbers: {my_fav_numbers}")

friend_fav_numbers = {4, 5, 6, 7, 8, 9, 10}
print(f"friend_fav_numbers: {friend_fav_numbers}")

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("------------------------------------------")

print(f"my_fav_numbers final: {my_fav_numbers}")
print(f"friend_fav_numbers final: {friend_fav_numbers}")
print(f"union of my_fav_numbers and friend_fav_numbers: {our_fav_numbers}")