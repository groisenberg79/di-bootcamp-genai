# Challenge 1: Letter Index Dictionary
# Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).



# Key Python Topics:

# User input (input())
# Dictionaries
# Loops (for loop)
# Conditional statements (if, else)
# String manipulation
# Lists


# Instructions:
# 1. User Input:

# Ask the user to enter a word.
# Store the input word in a variable.
# 2. Creating the Dictionary:

# Iterate through each character of the input word using a loop.
# And check if the character is already a key in the dictionary.

#     * If it is, append the current index to the list associated with that key.
#     * If it is not, create a new key-value pair in the dictionary.
# Ensure that the characters (keys) are strings.
# Ensure that the indices (values) are stored in lists.
# 3. Expected Output:

# For the input “dodo”, the output should be: {"d": [0, 2], "o": [1, 3]}.
# For the input “froggy”, the output should be: {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}.
# For the input “grapes”, the output should be: {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}.

user_letters_dict = dict()

user_word = input("Enter a word: ")

# create the dictionary 

for index, letter in enumerate(user_word):          # <-- loop through each (index, letter) pair in enumerate(user_word)
    if letter in user_letters_dict:                 # <-- check if the key is already in the dict
        user_letters_dict[letter].append(index)     # <-- if so, append the index of its occurance to existing value (a list of indexes)
    else:
        user_letters_dict[letter] = [index]         # <-- if not, create a new key with this letter;
                                                    #     its value will be a list whose only element is the corresponding index  

print(f"the resulting dictionary: {user_letters_dict}")

# Challenge 2: Affordable Items
# Goal: Create a program that prints a list of items that can be purchased with a given amount of money.

# Key Python Topics:

# Dictionaries
# Loops (for loop)
# Conditional statements (if, else)
# String manipulation (replace())
# Type conversion (int())
# Lists
# Sorting (sorted())


# Instructions:
# 1. Store Data:

# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.
# 2. Data Cleaning:

# You need to clean the dollar sign and the commas using python. Don’t hard code it.
# 3. Determining Affordable Items:

# create a list called basket and add there the items that you can buy with the money you have on the wallet
# Don’t forget to update the wallet after buying an item.
# If the basket is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, print the basket list in alphabetical order.
# 4. Examples:

# Given:
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"

# The output should be: ["Bread", "Fertilizer", "Water"].

# Given:
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"

# The output should be: ["Apple", "Bananas", "Fan", "Honey", "Spoon"].

# Given:
# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"

# The output should be: "Nothing".


def clean(money_string): #<-- eliminate occurances of '$' and ',' in the string and returns the corresponding integer
    return int(money_string.replace("$", "").replace(",", ""))

def dict_cleaning(items_purchase):              #<-- turn every money string into an int
    for key, value in items_purchase.items():   #<-- loop through each (item, price) pair
        items_purchase[key] = clean(value)      #<-- substitute old string for corresponding int


def buy_items(items_purchase, wallet):  #<-- buy items according to priority
    clean_wallet = clean(wallet)   
    dict_cleaning(items_purchase)
    basket = list()                     #<-- initialize basket of purchases
    for item in items_purchase.keys():  #<-- loop through each potential item purchase in dict
        price = items_purchase[item]
        if price <= clean_wallet:       #<-- if there is still sufficient money in the wallet
            basket.append(item)         #<-- put it in the basket
            clean_wallet -= price       #<-- update wallet after purchase of item
    return basket


def print_basket(basket):   #<-- print resulting basket after purchases
    if basket:
        print(sorted(basket))
    else:
        print("Nothing")


def main():

    items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
    wallet = "$300"
    basket = buy_items(items_purchase, wallet)
    print_basket(basket)

    items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
    wallet = "$100"
    basket = buy_items(items_purchase, wallet)
    print_basket(basket)
    
    items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
    wallet = "$1"
    basket = buy_items(items_purchase, wallet)
    print_basket(basket)


main()

