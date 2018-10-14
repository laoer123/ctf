#!usr/bin/python  
#-*- coding:utf-8 -*-  
import md5
import string

for i in string.uppercase:
    for j in string.uppercase:
        for k in string.uppercase:
            a='TASC'+i+'O3RJMV'+j+'WDJKX'+k+'ZM'
            b=md5.md5(a).hexdigest()
            if(b[0:5]=='e9032'):  
                print b
