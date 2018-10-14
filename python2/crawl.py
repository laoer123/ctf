# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:12:52 2018

@author: laoer123
"""

import requests
import re
from bs4 import BeautifulSoup as bs




def crawler():
    num = '48151'
    url = 'http://www.heibanke.com/lesson/crawler_ex00/'+str(num)
    while True:
        r = requests.get(url).text
        #print r
        if '下一个你需要输入的数字是' not in r:
            print num
            break
        else:
            soup = bs(r,"html.parser")
            info = soup.h3.string
            print info.encode('UTF-8')
            p = re.compile(r'\d+')
            num = p.findall(str(info))
            url = 'http://www.heibanke.com/lesson/crawler_ex00/'+''.join(num)
            print url
            

    
    '''
    while True:
        try:
            r = requests.get(url).content
            soup = bs(r,"html.parser")
            info = soup.find(url,{'class':"listing"}).find_all('h3')
            for i in info:
                print i
            if content.findall('下一个你需要输入的数字是')
        except:
            #continue
    '''

if __name__ == '__main__':
    crawler()