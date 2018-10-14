# -*- coding: utf-8 -*-
import sys
print '输入a:'
a = sys.stdin.readline()

n = len(a.split()[::-1][0])
print n

#print ''.join(each[-1]) for each in a.strip('.')