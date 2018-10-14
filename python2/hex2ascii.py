# -*- coding:utf-8 -*-

import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

# a = '36C95D99E921722C'
#
# b = [a[i:i+2] for i in range(0,len(a)) if i%2 == 0]
#
# for i in b:
#     #print i
#      print chr(int(i,16))

a = "36C95D99E921722C"
al = []
for i in range(0, len(a), 2):
    b = a[i:i+2]
    al.append(chr(int(b, 16)))
print ''.join(al)