#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Four
02.10.2023
"""

# Creating a Tuple.
my_tuple = ("John", "Mark", "Lio")

# Creating a Set.
my_set = {"Wick", "Williams", "Saint"}

# Converting a tuple into a list and assigning a variable.
list_from_tuple = list(my_tuple)

# Using append to add an element since I converted my tuple into a list.
list_from_tuple.append("Famous")

# Converting the list back into a tuple.
tuple_from_list = tuple(list_from_tuple)

# Adding an element to my set.
my_set.add("Insidious")

# Combining my_set and tuple_from_list and giving it the "Combined" variable
combined = my_set.union(tuple_from_list)

# Print the type of my_tuple my_set list_from_tuple tuple_from_list and Combined.
print(type(my_tuple))
print(type(my_set))
print(type(list_from_tuple))
print(type(tuple_from_list))
print(type(combined))

# Print the length.
print(len(my_tuple))
print(len(my_set))
print(len(list_from_tuple))
print(len(tuple_from_list))
print(len(combined))
