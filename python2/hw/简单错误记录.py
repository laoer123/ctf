'''
E:\V1R2\product\fpgadrive.c   1325
'''

import sys
d = {}
name = []
while True:
    try:
        for w in raw_input().split(' '):
            v = w
            #a = v[0].split('\\')[-1]
            print v
            if len(a) >= 16:
                a = a[-16:]
            v1 = a + '' + str(v[-1])
            if v1 not in d.keys():
                name.append(v1)
                d[v1] = 1
            else:
                d[v1] += 1
            break
    except:
        break
for item in name[-8:]:
    sys.stdout.write(item + ' ' +str(d[item]) + '\n')
    #print item + ' ' + str(d[item])