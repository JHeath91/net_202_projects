#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
03.10.2023
"""

FILE1 = "list_of_servers.txt"

FILE2 = "new_list_of_servers.txt"

New_server = ["Windows", "Linux"]


# Function to that opens the file as a list.
def server_name_list(file):
    with open(file, "r") as serv:
        server_list = serv.read().splitlines()
        return server_list


# Function to show how many servers are in the file.
def number_of_servers(server_list):
    num = len(server_list)
    return num


# Function that creates a new txt file.
def new_server_file(file, data):
    with open(file, "w") as new_list:
        for s in range(len(data)):
            new_list.write(f"{data[s]}\n")


# Function that adds 2 servers to the new file
def add_new_server(file_path, new_server):
    with open(file_path, 'a') as new_list:
        for s in range(len(new_server)):
            new_list.write(f"{new_server[s]}\n")


# Main man
def main():
    data = server_name_list(FILE1)
    print(data)
    print(number_of_servers(data))
    new_server_file(FILE2, data)
    add_new_server(FILE2, New_server)


main()
