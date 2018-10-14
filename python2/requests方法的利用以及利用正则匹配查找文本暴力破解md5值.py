#coding : utf8
import requests
import re
import hashlib
import itertools
s = requests.session()  //建立一个session对话
url = "http://106.75.67.214:2050/?pass=bee7a613a8fa4f2f"
data = {'PHPSESSID':'6h7b4caq8bo41i3m5fg2983cq5'}
content = s.get(url=url,data=data)
target = re.findall("sh\"\>(.*)\<",content.text) 
target = target[0]
poc = re.findall("code\"\>(.*)\<",content.text)
str1 = poc[0]
a = [''.join(x) for x in itertools.permutations(str1, 9)]  //join方法是通过指定的字符串来连接序列元素从而构成新字符串,permutations用来生成无重复字符的元组
for i in range(0,len(a)):
final = hashlib.md5(a[i])
if final.hexdigest() == target:
flag = s.get(url="http://106.75.67.214:2050/?code="+a[i])
print flag.content
print flag.headers