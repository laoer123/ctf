#coding:utf-8
import tarfile
for i in range(1,300)[::-1]:
    file = tarfile.open("shell"+str(i)+"tar.gz")
    file.extractall()
    file.close()