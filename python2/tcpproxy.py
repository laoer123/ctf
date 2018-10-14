#coding:utf-8

from socket import *
from sys import *

def Usage():
	print '[Usage]TCPproxy.py [LocalPort] [TargetHost] [TargetPort]'

try:
	THOST = argv[2]
	TPORT = int(argv[3])
except:
	print 'Please input pram.'

Main_Socket = socket(AF_INET,SOCK_STREAM)
RemoteSocket = socket(AF_INET,SOCK_STREAM)



def SetSocket(PORT):
	Main_Socket.bind(('127.0.0.1',PORT))
	Main_Socket.listen(1)

def FarwardData(Data):
	RemoteSocket.connect(THOST,TPORT)
	RemoteSocket.send(Data)
	Rdata = RemoteSocket.recv(1024)
	RemoteSocket.close()
	return Rdata
	
def Main_Handle():
	MainSock,MainAddr = Main_Socket.accept()
	print 'Connected by ',MainAddr
	while True:
		Ldata = MainSock.recv(1024)
		Rdata = FarwardData(Ldata)
		#转发ldata
		#接收响应
		MainSock.send(Rdata)
		
if __name__ == '__main__':
	try:
		LPORT = int(argv[1])
		SetSocket(LPORT)
		Main_Handle()
	except:
		Usage()