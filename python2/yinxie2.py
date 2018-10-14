from PIL import Image
from zlib import *
//二维码提取
data = open('d:\\201509291506131928.png','rb').read()[0x15AFFB:]
data = decompress(data)
 
img = Image.new('1', (25,25))
d = img.load()
for n,i in enumerate(data):
   d[(n%25,n/25)] = int(i)*255
 
f = open('flag1.png','wb')
img.save(f)
