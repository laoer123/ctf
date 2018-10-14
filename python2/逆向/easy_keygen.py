# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:08:33 2018

@author: laoer123
"""
s1 = []
serial = '5B,13,49,77,13,5E,7D,13'
s1 = serial.split(',')
#print s1

name = ''

a = [16,32,48]

i = 0
for index in range(len(s1)):
    if i >= 3:
        i = 0
    name += chr(int(s1[index],16) ^ a[i])
#    asc = int(serial[index],16) ^ a[i]
    i += 1
#    index += 1
#    print asc
print name
