# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

# What is a float?
# Answer:   A float (short for floating-point number) in Python is a data type 
#           used to represent real numbers that have a fractional, or decimal, component.
#           Floats are defined by the presence of a decimal point (e.g., 3.14) or
#           by the use of the scientific notation (e.g., 2e2, which is 200.0)

# What’s the difference between a float and an integer?
# Answer:   integers are used to represent whole numbers, 
#           while floats are used to represent real numbers with fractional components.
#           Formally, integers are numbers without a decimal point, while 
#           floats either have decimal points or use scientific notation.

number_list = []
for i in range(1, 6):
    number_list.append(i)
    if i < 5:
        number_list.append(i + 0.5)

print(number_list)
    