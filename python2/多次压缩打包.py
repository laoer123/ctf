#coding:utf-8
import tarfile
for i in range(1,2):
    tfile = tarfile.open("shell0.tar.gz","w:gz") #打包压缩
    tfile.add("flag.py")
    tfile.close()

for i in range(1,300):
    tfile = tarfile.open("shell"+str(i)+".tar.gz","w:gz")
    tfile.add("1.php")
    tfile.add("shell"+str(i-1)+".tar.gz")
    tfile.close()