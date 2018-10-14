import base64
import md5

key = '123'
s0 = 'system'
tmp = ''
for i in s0:
    tmp += chr(ord(i)+10)
#print tmp

txt_b64 = 'MTIzNDU2Nzg='
txt = base64.b64decode(txt_b64)
rnd = txt[0:4]
txt1 = txt[4:]
#print rnd,txt1

key = rnd+key

m = md5.new()
m.update(key.encode(encoding='utf-8'))
print m.hexdigest()

