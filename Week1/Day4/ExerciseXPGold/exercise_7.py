# Exercise 7: Min, Max, Sum
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
def main():

    number_list = [x for x in range(1, 1000001)]

    minimum = min(number_list)
    maximum = max(number_list)

    print(f"min = {minimum}, max = {maximum}")

    summation = sum(number_list)
    print(f"the sum of all numbers from 1 to 1000000 is {summation}")

main()