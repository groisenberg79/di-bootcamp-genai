# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.

# Test Data
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87

# The greatest number is: 87

def main():
    user_numbers = list()
    user_numbers.append(int(input("Enter the 1st number: ")))
    user_numbers.append(int(input("Enter the 2nd number: ")))
    user_numbers.append(int(input("Enter the 3rd number: ")))
    print(f"The greatest number is: {max(user_numbers)}")

main()

    