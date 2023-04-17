#!/usr/bin/env python3

"""
Jesse Heath
Assignment_Five
04.10.2023
"""

# Imports
from urllib3 import disable_warnings
disable_warnings()
from pprint import pprint
import json
import requests


# Things from Postman
url = "https://sandboxdnac2.cisco.com:443/dna/intent/api/v1/network-device"

payload={}
headers = {
  'x-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MjQxOTIzZTU3MjU5NTA2YTU2YjRhYTEiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYyM2YwMjlhNTcyNTk1MDZhNTZhZDljNCJdLCJ0ZW5hbnRJZCI6IjYyM2YwMjk4NTcyNTk1MDZhNTZhZDliZCIsImV4cCI6MTY4MTE4MTIxMSwiaWF0IjoxNjgxMTc3NjExLCJqdGkiOiI5YzgzYTRkMS0zYTU2LTQ3NjUtYTM2Zi03YTA4ZDNkYTk3NjUiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.kLcPIKYFIRi0aKtUFBSabnRZmASxHVX8aO7FYu2mXkkKoBbgWJ5IsOTUu3ZUuIqYmoaDcxPovVursteFhaos4y0gD879ItYxgcRIj1ciHYZhLcW8PK5MB3MBU4uguUDY3qsP14brDsCRYEjssrrHzBK3vZLugrYVq-EOuNugJnaT25f-o49poG9LsJVn0_55hi7LDURtHIuhbFT9aGlkkL0fDlfoVFtlENNsq3JUw6dVkIA703OQCN2iViGhDi3J9ZfkelUve5TbO4F9UHR6V_9mkKm1RdWq9pkgJNFbveVPvSDqsDpPUKKF-onVujmJqFoZmdEiKYzQkocT8e6g6g',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

response_converted = json.loads(response.text)


# Pretty printing the dict
pprint(response_converted)
print()

# Giving the dict a variable
data = response_converted['response']


# For loop for getting hostname and ip addresses
for items in data:
  h = items.get('hostname')
  i = items.get('managementIpAddress')
  if type(h) == str:
    print(f'{h} has an ip of {i}')
print()

# For loop for getting roles
for items in data:
  h = items.get('hostname')
  r = items.get('role')
  if r == 'ACCESS':
    print(f'{h} has the role of {r}')