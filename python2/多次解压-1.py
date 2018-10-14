#codingutf-8
import tarfile
for i in range(666,0,-1):
    file = tarfile.open(str(i)+".tgz")
    file.extractall()
    file.close()