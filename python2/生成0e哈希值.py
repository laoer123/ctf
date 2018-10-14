#coding:utf-8
import hashlib
import itertools
def go():
    payload = [c for c in "qwertyuioplkjhgfdsazxcvbnm123654789"]
    i = 0
    print payload
    for j in itertools.product(payload,repeat=30): #repeat参数指定长度
        payloads = "".join(j)
        #print pow
        #i = i+ 1
        #if i == 10:
        #    break
        str1 = hashlib.md5(payloads).hexdigest + "SALT"
        str2 = hashlib.md5(str1)
        if (str2[0]=="0") & (str2[1]=="e") & (str2[2:].isdigit()):
            print payloads
go()