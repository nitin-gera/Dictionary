# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:02:49 2018

@author: nitingera
"""

dt_group_tuple= ("deepika", "kranti", "rupesh", "nitin", "devesh", "neha", "anu")
dt_group_list= ["deepika", "kranti", "rupesh", "nitin", "devesh", "neha", "anu"]

print("tuple", dt_group_tuple)
print("list", dt_group_list)
print(dt_group_tuple[1:3])
print(dt_group_list[2:])


#ctr = 0
#
#while(ctr < len(dt_group_tuple)):
#   print("Tuple", dt_group_tuple[ctr])
#   print("List", dt_group_list[ctr])
#   ctr += 1

scores = (10500, 11000, 12000, 15000, 9000, 950)

print("Min:", min(scores))
print("Max:", max(scores))

dt_group_tuple[0] = "Chudail"
dt_group_tuple = list(dt_group_tuple)
dt_group_tuple[0] = "Chudail"

print(dt_group_tuple)
