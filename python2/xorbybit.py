#!usr/bin/python  
#-*- coding:utf-8 -*-  

f_a=open('miwen.txt','rb')  
f_b=open('mingwen.txt','rb')  

a="".join(f_a.readlines())
b="".join(f_b.readlines())  
print a
print b
s=''  
for i,j in zip(a,b):  
    s+=chr(ord(i)^ord(j))  
print s
