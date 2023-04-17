#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
03.06.2023
"""
import pprint


# Data
windows_servers = {'management01': '10.10.10.2', 'sccm01': '10.10.10.3', 'domaincontroller01': '10.10.10.4',
                  'domaincontroller02': '10.10.10.5', 'sql01': '10.10.10.6', 'exchange01': '10.10.10.7'}


linux_servers = {'application01': '10.10.20.2', 'ftp01': '10.10.20.3', 'vulnscanner01': '10.10.20.4',
                'ldap01': '10.10.20.5', 'dns01': '10.10.20.6', 'dns02': '10.10.20.7',
                'dhcp01': '10.10.20.8'}


# Total Number Of Servers.
def num_of_servers():
    len(windows_servers)
    len(linux_servers)
    print(f"Number of Windows Servers: {len(windows_servers)}")
    print(f"Number Of linux Servers: {len(linux_servers)}")


# Adding A New Server To the List.
def add_windows_server(name, ip,):
    new_server = {"server_name": name, "ip_address": ip}
    windows_servers[name] = ip
    print("Updated Server List")
    pprint.pprint(windows_servers)


# Lists All servers By Ip Addresses
def server_ips():
    total_ips = list(windows_servers.values()) + list(linux_servers.values())
    print(f"All Ip Addresses: ")
    print(total_ips)


# Lists All Servers By Name
def server_names():
    all_names = list(windows_servers.keys()) + list(linux_servers.keys())
    print("Server Names: ")
    print(all_names)


# The Main Man
def main():
    num_of_servers()
    add_windows_server("test01", "192.168.1.111")
    server_ips()
    server_names()


main()






