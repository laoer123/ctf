# Casare Algorithm

def convert(c, key, start = 'a', n = 26):
    a = ord(start)
    offset = ((ord(c) - a + key)%n)
    return chr(a + offset)
def caesarEncode(s, key):
    o = ""
    for c in s:
        if c.islower():
            o+= convert(c, key, 'a')
        elif c.isupper():
            o+= convert(c, key, 'A')
        else:
            o+= c
    return o
def caesarDecode(s, key):
    return caesarEncode(s, -key)
if __name__ == '__main__':
    #key = 3
    #s = 'This is Casare Algorithm.'
    s = 'T?^i\?fB^ArfO*DqS-f=L@@OMePHPA^/NfLIK*/OTtDMPOP.JN*'
    #e = caesarEncode(s, key)
    for key in range(1,27):
        d = caesarDecode(s, key)
        print d
    #print e
    #print d
