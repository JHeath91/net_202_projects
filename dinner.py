#!/usr/bin/env python3

def cooking_method(type_of_cooker):
    print(f'Cooking up a pizza using a {type_of_cooker}')


def pizza(pizza_toppings):
    print(f'Making a pizza with these toppings {pizza_toppings}')


def a_different_function():
    print('You wont need me for assignment ten')


def main():
    cooking_method('Microwave')
    pizza('Sausage')
    a_different_function()


if __name__ == '__main__':
    main()
