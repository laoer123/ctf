# Casare Algorithm
import base64

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
    s = 'LyjtL3fvnSRlo2xvKIjrK2ximSHkJ3ZhJ2Hto3x9'
    #e = caesarEncode(s, key)
    for key in range(1,27):
        d = caesarDecode(s, key)
        print base64.b64decode(d)
    #print e
    #print d
