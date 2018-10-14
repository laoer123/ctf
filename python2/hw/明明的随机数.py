import sys
while True:
    try:
        a = sys.stdin.readline()
        if a == "":
            break
        c = []
        for i in range(int(a)):
            b = sys.stdin.readline()
            c.append(int(b))
        c = list(set(c))
        c.sort()
        for i in c:
            print i
    except:
        break
