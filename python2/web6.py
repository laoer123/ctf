#coding:utf-8
import requests,base64
import re
import pwn
url='http://120.24.86.145:8002/web6/'
value=[0]*1000000
s=requests.Session()
content = s.post(url)
html = content.headers['flag']
flag  = base64.b64decode(base64.b64decode(html)[-8:])
#print flag
data = {'margin':flag}
content = s.post(url,data=data)
print content.text
