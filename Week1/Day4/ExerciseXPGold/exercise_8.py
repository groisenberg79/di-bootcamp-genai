# Exercise 8 : List and Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.

# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def main():

    user_numbers = input("Enter a sequence of integers separeted by commas: ")

    number_list = [num.strip() for num in user_numbers.split(',') ]
    generator_expression = (num.strip() for num in user_numbers.split(','))

    print(number_list)
    print(tuple(generator_expression))

main()