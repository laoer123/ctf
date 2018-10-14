# -*- coding: utf-8 -*-
import sys
def count(a,strA):
    s = []
    for i in a:
        s.append(i)

    index = 0
    for j in range(0,len(s)):
        if s[j].lower() == strA.lower():
            index += 1
    return index

aa = sys.stdin.readline()
bb = raw_input()
print count(aa,bb)