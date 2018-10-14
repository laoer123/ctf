# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:12:52 2018

@author: laoer123
"""

import requests
import re
from bs4 import BeautifulSoup as bs




def crawler():
    url = 'http://www.heibanke.com/lesson/crawler_ex01/'
    for num in range(1,31):
        r = requests.post(url,data = {"username":"test","password":num}).text
        #print r
        if '您输入的密码错误' not in r:
            print 'the number is %d' % num
            break
            

    
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