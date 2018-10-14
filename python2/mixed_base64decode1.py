#!/usr/bin/env python

import base64
#import requests

#def download(url):
#    return requests.get(url).text

steps = []
#url = "http://ctf.nuptzj.cn/static/uploads/3e5c0c7045f2a81363a45d97d69911e3/code.txt"

print "[+] Downloading encrypted file..."
with open("code.txt","rb") as f:
    p=f.read()
#p = download(url)
n = ""

while True:
    # Base16
    try:
        print "[?] using base16 deocde"
        n = base64.b16decode(p)
        print "[+] %s" % (n)
        steps.append(16)
        p = n
        continue
    except:
        pass
    # Base32
    try:
        print "[?] using base32 deocde"
        n = base64.b32decode(p)
        print "[+] %s" % (n)
        steps.append(32)
        p = n
        continue
    except:
        pass
    # Base64
    try:
        print "[?] using base64 deocde"
        n = base64.b64decode(p)
        print "[+] %s" % (n)
        steps.append(64)
        p = n
        continue
    except:
        pass
    break

print "[+] flag found : %s" % (n)
print "[+] steps : %s" % (steps)
