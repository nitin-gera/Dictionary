# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:28:52 2018

@author: nitingera
"""

employee = {"Name": "Nitin",
            "Staff no": 214028,
            "Joining year": 2008,
            "Salary": "meagre"}

print(employee["Salary"])

employee["Salary"] = "Pathetic"

print(employee)

del employee["Joining year"]

print(employee)

print(str(employee))

print(employee.get("Salary"))
print(employee.items())
print(employee.values())
print(employee.keys())

for pair in employee.values():
    print(pair)