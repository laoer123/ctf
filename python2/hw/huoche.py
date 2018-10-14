import sys
import random

while True:
    try:
        l = []
        b = []
        c = []
        d = []
        a = int(raw_input())
        #for i in range(0,a):
        b = raw_input().split(' ')
        for i in b:
            l.append(int(i))
        #print l
        c,d = b
        #for i in c[len(c)]:
        while len(c):
            e = random.randint(len(c))
            print c[e]
            d.append(c[e])
            c.pop(e)
            print d

    except:
        break
