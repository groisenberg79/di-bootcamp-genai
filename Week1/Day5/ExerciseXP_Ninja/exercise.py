# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = cars.split(", ")
print(f"There are {len(cars_list)} manufactures in the list.")
cars_sorted_inverse = sorted(cars_list, reverse=True)
print(cars_sorted_inverse)

count_o = 0
for manufacturer in cars_list:
    if "o" in manufacturer:
        count_o += 1
print(f"There are {count_o} manufacturers with \"o\".")

count_not_i = 0
for manufacturer in cars_list:
    if "i" not in manufacturer:
        count_not_i += 1
print(f"{count_not_i} manufacturers do not have an \"i\".")

car_list_repeated = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
car_set = set(car_list_repeated)
print(car_set)
car_list_without_rep = list(car_set)
print(car_list_without_rep)
for index, car in enumerate(car_list_without_rep):
    if index != len(car_list_without_rep) - 1:
        print(car, end=", ")
    else:
        print(car)
print(f"There are {len(car_list_without_rep)} car companies.")

car_list_with_reversed_letters = list()
for car in cars_list:
    car_reversed = car[::-1]
    car_list_with_reversed_letters.append(car_reversed)

print(sorted(car_list_with_reversed_letters))