import gzip
import os
def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    #��ȡ�ļ������ƣ�ȥ��
    g_file = gzip.GzipFile(file_name)
    #����gzip����
    open(f_name, "w+").write(g_file.read())
    #gzip������read()�򿪺�д��open()�������ļ��С�
    g_file.close()
    #�ر�gzip����

un_gz(r'd:\1.gz')
