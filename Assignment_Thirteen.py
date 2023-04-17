#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
04.07.2023
"""

# Making a custom type error message.
try:
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    result = number_1 + number_2
    print(f"The result is {result}")
except ValueError:
    print("Please enter a valid number")


# Putting the custom error message in a while loop.
while True:
    try:
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
        result = number_1 + number_2
        print(f"The result is {result}")
    except ValueError:
        print("Please enter a valid number")
    else:
        break
