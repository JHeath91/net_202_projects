#!/usr/bin/env python3


# Jesse Heath
# Assignment_One
# 01/30/2023

# Making Variables
word_one = input("Enter A Word: ")
word_two = input("Enter A Second Word: ")
number = int(input("Enter A Number: "))

# Using if/else statements to compair string lengths.
if len(word_one) == len(word_two):
    print("Equal")
else:
    if len(word_one) > len(word_two):
        print(f"{word_one} is the longest string.")
    elif len(word_two) > len(word_one):
        print(f"{word_two} is the longest string.")

# Using if/elif statements to check if the integer is greater than the word length
if len(word_one) < number:
    print(f"{number} is {number - len(word_one)} characters larger than {word_one}")
elif len(word_one) > number:
    print(f"{number} is shorter than {word_one}")

if len(word_two) < number:
    print(f"{number} is {number -len(word_two)} characters larger than {word_two}")
elif len(word_two) > number:
    print(f"{number} is shorter than {word_two}")

# Checking if the user inputs have a specific letter in them.
if word_one.find("i") != -1:
    print(f"i is located inside {word_one}")
else:
    print(f"i is not located inside {word_one}")
if word_two.find("i") != -1:
    print(f"i is located inside {word_two}")
else:
    print(f"i is not located inside {word_two}")
