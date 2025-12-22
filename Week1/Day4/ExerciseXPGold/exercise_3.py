# Exercise 3: Check the index
# Instructions
# Using this variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.

# Example: if input is 'Cortana' we should be printing the index 1

def main():
    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
    user_name = input("Enter your name: ").capitalize()
    in_list = False
    for index, name in enumerate(names):
        if name == user_name:
            in_list = True
            print(f"index in the list: {index}")
            break
    if in_list == False:
        print(f"'{user_name}' not in the list.")

main()

