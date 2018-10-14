#coding: utf8
import sys
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
 
class prpcrypt():
    def __init__(self, key):
		self.key = key
        self.mode = AES.MODE_CBC
		#���ܺ��������text����16�ı����������ı�text����Ϊ16�ı����������ǾͲ���Ϊ16�ı���
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        #������Կkey ���ȱ���Ϊ16��AES-128����24��AES-192������32��AES-256��Bytes ����.ĿǰAES-128�㹻��
        length = 16
        count = len(text)
	if(count % length != 0) :
        	add = length - (count % length)
	else:
		add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #��ΪAES����ʱ��õ����ַ�����һ����ascii�ַ����ģ�������ն˻��߱���ʱ����ܴ�������
        #��������ͳһ�Ѽ��ܺ���ַ���ת��Ϊ16�����ַ���
        return b2a_hex(self.ciphertext)
     
    #���ܺ�ȥ������Ŀո���strip() ȥ��
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')
 
if __name__ == '__main__':
	key = "\x2b"+"\x7e"+"\x15"+"\x16"+"\x28"+"\xae"+"\xd2"+"\xa6"+"\xab"+"\xf7"+"\x15"+"\x88"+"\x09"+"\xcf"+"\x4f"+"\x3c"
	usr = "WelcomeB0dy"
    pc = prpcrypt(key)      #��ʼ����Կ
	m1 = hashlib.md5()
	m1.updata(usr)
    e = pc.encrypt("0123456789ABCDEF")
    d = pc.decrypt(e)                     
    print e, d
    e = pc.encrypt("00000000000000000000000000")
    d = pc.decrypt(e)                  
    print e, d