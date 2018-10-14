import random
from base64 import *
result={
    '16':lambda x:b16decode(x),
    '32':lambda x:b32decode(x),
    '64':lambda x:b64decode(x),  
    }

#flag=b"nctf{**********}"

with open("code.txt","rb") as f:
    flag=f.read()
    
for i in range(10):
    a=random.choice(['16','32','64'])
    flag=result[a](flag)

print flag
