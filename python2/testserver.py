#coding:utf-8

from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(('',6666))
s.listen(1)
while True:
	sock,addr = s.accept()
	print 'Connected by ',addr
	data = sock.recv(1024)
	print data
	sock.send('Yes')
