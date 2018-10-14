import sys

while True:
    try:
        a = raw_input()
        b = a.split('.')
        if int(b[-1])>=5:
            b[0]=int(b[0])+1
        print b[0]
        print b
    except:
        break