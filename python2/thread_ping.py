#coding:utf-8

from threading import Thread
from time import sleep
from os import system
from time import time

def ThreadHandle(name):
	#print 'this is test!'
	system('ping '.name)
	now2 = time()
	print (now2 - now1)
	
if __name__=='__main__':
	now1 = time()
	for i in range(5):
		t=Thread(target=ThreadHandle,args=('www.baidu.com',))
		sleep(0.1)
		t.start()