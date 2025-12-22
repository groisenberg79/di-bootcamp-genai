# Exercise 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

def main():
    for num in range(1500, 2501):
        if num % 5 == 0 or num % 7 == 0:
            print(num, end=" ")

main()
