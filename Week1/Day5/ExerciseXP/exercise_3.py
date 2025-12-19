# 🌟 Exercise 3: Zara
# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.



# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.


# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

brand = {"name": "Zara", 
         "creation_date": 1975, 
         "creator_name": "Amancio Ortega Gaona",
         "type_of_clothes": ["men", "women", "children", "home"], 
         "international_competitors": ["Gap", "H&M", "Benetton"], 
         "number_stores": 7000,
         "major_color":{"France": ["blue"],
                        "Spain": ["red"],
                        "US": ["pink", "green"]
                        }
        }

brand["number_stores"] = 2
print("number of stores:", brand["number_stores"])
print()

print(f"Zara customers are {brand['type_of_clothes'][0]}, {brand['type_of_clothes'][1]} and {brand['type_of_clothes'][2]}.")
print()

brand["country_creation"] = "Spain"
print("country of creation:", brand["country_creation"])
print()

if brand["international_competitors"]:
    brand["international_competitors"].append("Desigual")
print("competitors:", brand["international_competitors"])
print()

del brand["creation_date"]

print(f"last international competitor: {brand['international_competitors'][-1]}")
print()

print("the major colors in the US are:", ", ".join(brand["major_color"]["US"]))
print()

print(f"number of keys in the dictionary: {len(brand.keys())}")
print()

print("here are the keys if the 'brand' dictionary:\n")
for key in brand.keys():
    print(key)







