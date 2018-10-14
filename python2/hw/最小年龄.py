
while True:
    try:
        l = []
        t = ()
        n = int(raw_input())
        for i in range(n):
            t = tuple(raw_input().split(' '))
            #print t
            l.append(t)
            #print l
        l1 = sorted(l,key=lambda d:int(d[2]))
        #print l1
        #if n > 3:
         #   print ' '.join(l1[0])
          #  print ' '.join(l1[1])
           # print ' '.join(l1[2])
        #else:
        for i in range(min(3,n)):
            print ' '.join(l1[i])
    except:
        break