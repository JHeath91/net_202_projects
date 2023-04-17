#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
03.24.2023
"""

from netmiko import ConnectHandler


# Template for Netmiko
cisco = {"device_type": "cisco_ios", "host": "ip_address", "username": "user_name", "password": "user_pass"}


cisco["host"] = "sandbox-iosxe-latest-1.cisco.com"
cisco["username"] = "admin"
cisco["password"] = "C1sco12345"


net_connect = ConnectHandler(**cisco)


create_loopback = ["interface loopback 50", "ip address 192.168.50.50 255.255.255.0"]

net_connect.send_config_set(create_loopback)

