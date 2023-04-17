#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Three
02.05.2023
"""

# List Of Malicious Ips.
malicious_external_ips = [    "66.228.47.75",    "27.2.184.137",    "133.242.18.121",    "116.85.70.163",
                              "105.213.66.241",    "5.2.247.126",    "103.232.202.66",    "194.87.185.93",
                              "116.85.34.221",    "183.79.208.49",    "103.85.71.76"]

# Creating a parameter list for malicious ips
list = malicious_external_ips

for ip in list:
    if ip.startswith("103") or ip.startswith("104"):
        continue
    elif ip.endswith("3") or ip.split(".")[1] == "85":
        continue
    else:
        print(f"Deny ip {ip}")

# Printing 4 spaces.
print("\n\n\n\n")

# List of current passwords.
password_list = ['P@ssw0rd', 'super_secretPass', 'Bacon','YoullNeverGuessThisPass','Pineappledoesntgoonpizza',
                 'HackersLOL', 'P@ss', 'randomlygener@ted', 'notsecure', 'emailifyouneedhelp']

# Making a list of password that do not meet system requirements.
insecure_passwords = []
for password in password_list:
    if len(password) < 12 or password != '!' or password != '@':
        insecure_passwords.append(password)

print("Passwords that do not conform to standards:")
for password in insecure_passwords:
    print(password)

print(f"Number of passwords that do not conform to standards:{len(insecure_passwords)}")
