import gzip
for i in range(1,1000):
    f = gzip.open('e:\666.tgz')
    file_content = f.read()
    f.close()
