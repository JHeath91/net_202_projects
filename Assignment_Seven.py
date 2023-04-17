

# Global Variables.
integer_additive = 7


# Main Function.
def main():
    users_name = name_input()
    get_length_of_list(create_a_list(print_output(users_name)))


# Name input Function.
def name_input():
    name = input("Please Enter your Name:")
    return name


# Prints out users input.
def print_output(users_name):
    user_string = f"The name entered is {users_name}"
    print(user_string)
    return user_string


# Turning the string into a list and splitting it.
def create_a_list(input_string):
    my_list = input_string.split()
    print(my_list)
    return my_list


# Getting the length of the list.
def get_length_of_list(my_list):
    list_length = len(my_list) + integer_additive
    print(list_length)


main()

