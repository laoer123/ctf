# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 10:25:15 2018

@author: laoer123
"""

import os

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

K=[]
for i in range(7):
    K.append(os.urandom(27))
m=open("flag","rb").read()
assert len(m)<54
m+=os.urandom(54-len(m))

test = "0b7361c8143e5935f9f5be3949cc07ed7a5ba6f258ebd91f29c5a7d16976f8dfb7fa422a6167281e573d015cc6d995841d5cab07923c".decode("hex")

for i in range(189):
    sa.append(random.choice(seed))
    K = ''.join(sa)
    m = fez(text,K)
    
print fez(test,K).encode("hex")
print fez(m,K).encode("hex")

