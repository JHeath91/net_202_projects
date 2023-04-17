#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
02.13.2023
"""

ip_addresses = ['10.77.48.123', '192.55.71.22', '192.168.33.22', '172.18.31.55', '.58.27.230.221', '109.22.57.3',
               '86.2.45.11', '192.168.10.4', '192.168.44.71', '172.204.2.5', '10.2.12.7', '192.202.47.18', '172.32.55.1']

# Creating a blank list and a count for specific ips.
private_ip = []
count = 0

# Using a for loop to get the ips that start with specific numbers and add them to the blank list.
for ip in ip_addresses:
    if ip.startswith('10.'):
        private_ip.append(ip)
        count += 1
    elif ip.startswith('192.168'):
        private_ip.append(ip)


# Using another for loop to get the ips in a specific range and add them to the blank list.
for ip in ip_addresses:
    if ip.startswith('172.') and int(ip.split('.')[1]) <=16:
        private_ip.append(ip)
    elif ip.startswith('172.') and int(ip.split('.')[1]) <=31:
        private_ip.append(ip)


# Results
print('Private IPs : ', private_ip)
print('Number of addresses that begin with 10.: ', count)

