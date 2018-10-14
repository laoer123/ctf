def checklen(s):
    if len(s) > 8:
        return True
    else:
        return False

def check2(s):
    flagup,flaglow,flagdigit,flagother = 0,0,0,0
    for i in s:
        if i.isupper():
            flagup = 1
        elif i.islower():
            flaglow = 1
        elif i.isdigit():
            flagdigit = 1
        else:
            flagother = 1
    if flagother+flagdigit+flaglow+flagup >= 3:
        return True
    else:
        return False

def check3(s):
    for i in range(len(s)-3):
        if s.count(s[i:i+3]) >1:
        #if s[i:i + 3].count(s[i]) > 2:
            return False
    return True

while True:
    try:
        s = raw_input()
        if checklen(s) and check2(s) and check3(s):
            print 'OK'
        else:
            print 'NG'
        #break
    except:
        pass
        #break

