#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
03.24.2023
"""
# Importing from file download
from dinner import cooking_method, pizza


# Function to convert F to C
def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5//9
    print(f"The best temperature to cook at is {celsius}c")
    return celsius


# Main Function
def main():
    cooking_method("Brick Oven")
    pizza("Beef, Onion")
    fahrenheit_to_celsius(450)


if __name__ == "__main__":
    main()
