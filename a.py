import csv
from pprint import pprint


def create_servers_dict():
    servers_dict = []
    with open('servers.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            servers_dict[row['Server']] = row['IP Address']
    pprint(servers_dict)


def create_os_lists():
    windows_servers = []
    linux_servers = []
    with open('servers.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "Windows" in row["Operating System"]:
                windows_servers.append(row['Server Name'])
            elif row['Operating System'] == 'Linux':
                linux_servers.append(row['Server Name'])
    print("Windows servers: ", windows_servers)
    print("Linux servers: ", linux_servers)


def main():
    create_servers_dict()
    create_os_lists()


main()
