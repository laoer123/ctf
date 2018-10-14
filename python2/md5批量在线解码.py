# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:39:41 2018

@author: laoer123
"""


import requests
from bs4 import BeautifulSoup
import optparse
import sys

def main():
  usage="[-m md5 decryption]"
  parser=optparse.OptionParser(usage)
  parser.add_option('-m',dest='md5',help='md5 decryption')
  f = open('1.txt','r')
  for i in f.readlines():
      md5 = str(i).strip('\n')
      if md5:
          Md5(md5)
      else:
        parser.print_help()
        exit()
 
def Md5(md5):
  header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
  data = {
    '__VIEWSTATE': '/wEPDwUKMTM4NTE3OTkzOWRkP4hmXYtPPhcBjbupZdLOLfmeTK4=',
    '__VIEWSTATEGENERATOR': 'CA0B0334',
    '__EVENTVALIDATION': '/wEWAwK75ZuyDwLigPTXCQKU9f3vAheUenitfEuJ6eGUVe2GyFzb7HKC',
    'key': '{}'.format(md5),
    'jiemi': 'MD5解密'
  }
  url = "http://pmd5.com/"
  r = requests.post(url, headers=header, data=data)
  sd = r.content.decode('utf-8')
  esdf = BeautifulSoup(sd, 'html.parser')
  for l in esdf.find_all('em'):
    g = l.get_text()
    print('--------[*]PMD5接口--------')
    print(g)
 
if __name__ == '__main__':
  main()

'''
s = 'd78b6f302l25cdc811adfe8d4e7c9fd34'
s1= ''

for i in range(0,len(s)):
    print s[0:i]+s[(i+1):len(s)]
'''