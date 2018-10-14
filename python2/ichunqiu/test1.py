# -*- coding: utf-8 -*



import requests

import string

from base64 import *



url = "http://70cbc6541eaa431496fd0b427cd68d43a0a76defc21b4703.game.ichunqiu.com/index.php?jpg=fl3g_ichuqiu.php"

cookie = requests.get(url).cookies['user']

txt = b64decode(cookie)

rnd = txt[:4]

ttmp = txt[4:]    #获取cookie从而得到rnd值(4位)和ttmp值(5位，即md5后的key的前五位)



keys = list('xxxxxx')



guest = list('guest')

for i in range(len(guest)):

    guest[i] = chr(ord(guest[i])+10)

for i in range(len(guest)):

    keys[i] = chr(ord(ttmp[i])^ord(guest[i]))    #根据源码，算出key的前五位（异或）



system = list('system')           #用已知信息（key值）来对system进行加密

for i in range(len(system)):

    system[i] = chr(ord(system[i])+10)

ttmp_new = ''

str = ''

letters = '1234567890abcdef'     #system有六位，但我们只知道五位的key，所以要爆破一下最后一位

for ch in letters:

    keys[5] = ch

    for i in range(len(system)):

        ttmp_new += chr(ord(keys[i]) ^ ord(system[i]))

    str = rnd + ttmp_new

    print b64encode(str)

    ttmp_new = ''
