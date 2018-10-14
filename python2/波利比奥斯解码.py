# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:32:17 2018

@author: laoer123
"""

a = []
s0 = ''
dic = {'11':'A','12':'B','13':'C','14':'D','15':'E','21':'F','22':'G','23':'H','24':'I/J','25':'K','31':'L','32':'M','33':'N','34':'O','35':'P','41':'Q','42':'R','43':'S','44':'T','45':'U','51':'V','52':'W','53':'X','54':'Y','55':'Z'}
#print dic

s = '3534315412244543_434145114215_132435231542'
s1 = s.split('_')
#print s1

for i in s1:
    for j in range(0,len(i)/2):
        a.append(i[j*2:(j+1)*2])
#print a

for i in a:
    s0 += ''.join(dic[i])
print s0.lower()