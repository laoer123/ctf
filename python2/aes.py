#encoding:utf-8 

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64

KEY='EaRncVfLgIPMaygA'
IV='1234567890123456'
#text='The answer is no'

#encryptor=AES.new(KEY, AES.MODE_CBC,IV)

#ciphertext=encryptor.encrypt(text)
ciphertext='kt1zBVG4Om1rVxe2ISqt1WFZ+tWvgNV3QygfrSlFRjI='
#print ciphertext
#print b2a_hex(ciphertext)

#IV=a2b_hex(IV)
#ciphertext=a2b_hex(ciphertext)
#print IV

""" 
上例中的key是16位, 还可以是24 或 32 位长度， 其对应为 AES-128, AES-196 和 AES-256. 
解密则可以用以下代码进行： 
""" 
decryptor = AES.new(KEY, AES.MODE_CBC,IV)
plain = decryptor.decrypt(base64.b64decode(ciphertext))
print plain