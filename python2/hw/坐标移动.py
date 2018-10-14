import sys
import re
while True:
    try:
        a = raw_input().split(';')
        #print a
        c = []
        for i in a:
            if re.match(r'^(A|D|W|S)\d+$',i):
                c.append(i)
        b = 0
        org = [0,0]
        for i in c:
            if re.match(r'^A\d+',i):
                b = int(i[1:])
                org[0] = org[0] - b
            elif re.match(r'^D\d+',i):
                b = int(i[1:])
                org[0] = org[0] + b
            elif re.match(r'^W\d+',i):
                b = int(i[1:])
                org[1] = org[1] + b
            elif re.match(r'^S\d+',i):
                b = int(i[1:])
                org[1] = org[1] - b
            else:
                continue
        print str(org[0])+','+str(org[1])
    except:
        break
