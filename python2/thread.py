# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:24:35 2018

@author: laoer123
"""

import requests
import threading
import time
import Queue
import re
from bs4 import BeautifulSoup as bs
import urllib
import base64
import os

#print os.getcwd()

class JianDan(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue
    def run(self):
        while not self._queue.empty():
            url = self._queue.get_nowait()
            self.spyder(url)
    def spyder(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'}
        #url = 'http://jandan.net/ooxx/page-30#comments'
        r = requests.get(url=url,headers=headers)
        #print r.status_code,len(r.content)
        #soup = bs(r.content,'lxml')
        #imgs = soup.find_all(name='src',attrs={})
        
        imgs = re.findall('"img-hash">(.*?)</span></p>',r.content)
        for img in imgs:
            img = 'http://'+base64.b64decode(img).split('//')[-1]
            print img
            name = img.split('/')[-1]
            filename='img/'+name
            #print filename
#            urllib.urlretrieve(img,filename='img/'+name)
            self.auto_down(img,filename)
    def auto_down(self,url,filename):
        try:
            urllib.urlretrieve(url,filename)
        except urllib.ContentTooShortError:
            print 'Network conditions is not good.Reloading.'
            auto_down(url,filename)

def main():
    os.chdir('E:\python\pycode\python2')
    queue = Queue.Queue()
    for i in range(1,33):
        queue.put('http://jandan.net/ooxx/page-'+str(i))
    
    threads = []
    thread_count = 5
    
    for i in range(thread_count):
        threads.append(JianDan(queue))
        
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
        
if __name__ == '__main__':
    main()

  
    
    
    
#spyder()