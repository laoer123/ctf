# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:14:17 2018

@author: laoer123
"""

import hashlib
import base64

s = 'GUYDIMZVGQ2DMN3CGRQTONJXGM3TINLGG42DGMZXGM3TINLGGY4DGNBXGYZTGNLGGY3DGNBWMU3WI==='
print base64.b32decode(s)

'''
while True:
    s = base64.b64decode(s)
    if 'flag' in s:
        print s
        break
    else:
        continue
'''

