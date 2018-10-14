# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 09:45:54 2018

@author: laoer123
"""

import os

text = "0b7361c8143e5935f9f5be3949cc07ed7a5ba6f258ebd91f29c5a7d16976f8dfb7fa422a6167281e573d015cc6d995841d5cab07923c".decode("hex")

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"

def xor(a,b):
    assert len(a)==len(b)
    c=""
    for i in range(len(a)):
        c+=chr(ord(a[i])^ord(b[i]))
    return c
def f(x,k):
    return xor(xor(x,k),7)

def round(M,K):
    L=M[0:27]
    R=M[27:54]
    new_l=R
    new_r=xor(xor(R,L),K)
    return new_l+new_r

def fez(m,K):
    for i in K:
        m=round(m,i)
    return m

sa = []
for i in range(189):
    sa.append(random.choice(seed))
    K = ''.join(sa)
    m = fez(text,K)
    if m == "f46d9ffa6a28a3fc2aa17c244ec29fc6a7bf5cac0da4489ad53782f1ef66597dc2928517b56693347ad468154e6f0f1ff8501fa6a1b1".decode("HEX"):
        
        
#    print K


s = ''
flag = ''
with open('C:\\1.txt','rb') as f:
    s = f.read()
#print s
print s
#length=len(s)
#print length
'''

i=0

while i<length:
    if ord(s[i])==0x64:
        flag += s[i-1]
    i=i+1

print flag

'''