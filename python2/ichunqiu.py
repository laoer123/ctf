# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 14:19:59 2018

@author: laoer123
"""


import os

s = ''
flag = ''
with open('C:\\Users\\laoer123\\Desktop\\blue_monday','r') as f:
    s = f.read()
#print s

length=len(s)

i=0

while i<length:
    if ord(s[i])==0x64:
        flag += s[i-1]
    i=i+1

print flag