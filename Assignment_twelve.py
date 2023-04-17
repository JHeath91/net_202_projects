#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
04.03.2023
"""

from netmiko import ConnectHandler


def a_user_name():
    username = input("Enter a User Name: ")
    return username


def user_password():
    password = input("Enter a Password: ")
    return password


def host_ip():
    hostname = input("Enter a Hostname or IP address")
    return hostname


def run_conf(hostname, username, password):
    cisco = {'device_type': 'cisco_ios',
        'host': '1.1.1.1',
        'username': username,
        'password': user_password
        # 'secret': 'mysecret'
    }

    cisco['host'] = hostname
    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_command("show running-config")
    return output


def saved_conf_file(config):
    with open("saved_config_file.txt", "w") as f:
        f.write(config)


if __name__ == '__main__':
    username = a_user_name()
    password = user_password()
    hostname = host_ip()
    output = run_conf(host_ip, username, password)
    saved_conf_file(run_conf)


