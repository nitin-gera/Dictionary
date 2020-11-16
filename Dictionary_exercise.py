# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:49:32 2018

@author: nitingera
"""
gpas = {
"Bob": 3.14,
"Mark": 3.45,
"Melissa": 3.98,
"Travis": 2.55,
"DeeDee":3.24, 
"Ian": 2.27
}

sum = 0

for gpa in gpas.values():
    sum += gpa

print("sum:", sum, "average:", sum/len(gpas))

print("Min gpa:", min(gpas.values()))
print("Max gpa:", max(gpas.values()))