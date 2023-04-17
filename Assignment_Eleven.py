#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
03.27.2023
"""

# Import
from pprint import pprint
import csv
filename = "servers.csv"


# Function to pprint all servers and ips
def new_server_dict():
    servers_dict = {}
    with open("servers.csv", "r") as data:
        for row in csv.DictReader(data):
            servers_dict[row["Server"]] = row["IP Address"]
    pprint(servers_dict)


# Function for a list of linux and windows servers.
def new_server_lists():
    windows_server = []
    linux_server = []
    with open("servers.csv", "r") as data:
        for row in csv.DictReader(data):
           if "Windows" in row["Operating System"]:
               windows_server.append(row["Server"])
           elif row["Operating System"] == "Linux":
               linux_server.append(row["Server"])
        print("Window Servers: ", windows_server)
        print("Linux Servers: ", linux_server)


# Function for server locations
def server_location():
    east_servers = 0
    west_servers = 0
    with open("servers.csv", "r") as data:
        for row in csv.DictReader(data):
            if row["Datacenter"] == "East":
                east_servers += 1
            elif row["Datacenter"] == "West":
                west_servers += 1
    print(f"Number of east servers: {east_servers}")
    print(f"Number of west servers: {west_servers}")


# Main
def main():
    new_server_dict()
    new_server_lists()
    server_location()


main()
