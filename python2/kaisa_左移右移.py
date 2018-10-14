# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:12:06 2018

@author: laoer123
"""

import re

s0 = 'lrua{1uy3yj9l-yw9u-48j2-uuj8-36h03706y7u7}'
#flag{1ae3ed9f-ec9a-48d2-aad8-36b03706e7a7}

s1 = re.findall('[a-z]',s0)
s1 = ''.join(s1)
print len(s1)
result = []

char = 'abcdefghijklmnopqrstuvwxyz'
for i in s1:
    s1_index = char.index(i)
#    print s1_index
    if s1_index % 2 == 0:
        s1_index += 6
        if s1_index > 25:
            s1_index -= 26
        result.append(char[s1_index])
    else:
        s1_index -= 6
        if s1_index < 0:
            s1_index += 26
        result.append(char[s1_index])

print len(result)
#print ''.join(result)