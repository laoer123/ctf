# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 10:37:27 2018

@author: laoer123
"""

import base64
import string
#import os
#import random

a='AAoHAR1XICMnIlBfUlRXXyBXJFRSUCRRI1RSJyQkIlYgU1EjURs='
b=string.lowercase

s=base64.b64decode(a)
flag=''

#for j in b:
#    for i in range(len(s)):
#        flag += chr(ord(s[i])^ord(j))
#print flag

#seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
#sa = []
#for i in range(26):
#    sa.append(random.choice(seed))
#    test = ''.join(sa)
#    for i in b:
#        for j in range(len(test)):
#            flag += chr(ord(test[j])^ord(i))
#    with open('C:\\2.txt','w') as f:
#        f.write(flag)
#    f.close()


for j in b:
    for i in range(len(s)):
        flag += chr(ord(s[i])^ord(j))
print flag