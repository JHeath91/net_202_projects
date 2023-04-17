#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Six
02.20.2023
"""


while True:
    ip = input("Please Enter Your IP: ")
    isValid = False
    octets = ip.split(".")
    if len(octets) == 4:

        for octet in octets:
            if int(octet) < 0 or int(octet) > 256:
                isValid = False
                break
            else:
                isValid = True
    else:
        isValid = False

    if isValid:
        print("Valid Ip")
        break
    else:
        print("Invalid IP. Try again")





