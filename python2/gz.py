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

# -*- coding: utf-8 -*- 
#~ #------------------------------------------------------------------
#~ module:wlab 
#~ Filename:wgetfilelist.py 
#~ Function : 
#~ def IsSubString(SubStrList,Str) 
#~ def GetFileList(FindPath,FlagStr=[]): 
#~ ����:��ȡָ��Ŀ¼���ض����͵��ļ����б� 
#~ Data: 2013-08-08,������ 
#~ Author:����ƽ 
#~ Email:wxp07@qq.com 
#~ #------------------------------------------------------------------
#~ #------------------------------------------------------------------
def IsSubString(SubStrList,Str): 
 ''''' 
 #�ж��ַ���Str�Ƿ��������SubStrList�е�ÿһ�����ַ��� 
 #>>>SubStrList=['F','EMS','txt'] 
 #>>>Str='F06925EMS91.txt' 
 #>>>IsSubString(SubStrList,Str)#return True (or False) 
 '''
 flag=True
 for substr in SubStrList: 
  if not(substr in Str): 
   flag=False
 return flag 
#~ #---------------------------------------------------------------------- 
def GetFileList(FindPath,FlagStr=[]): 
 ''''' 
 #��ȡĿ¼��ָ�����ļ��� 
 #>>>FlagStr=['F','EMS','txt'] #Ҫ���ļ������а�����Щ�ַ� 
 #>>>FileList=GetFileList(FindPath,FlagStr) # 
 '''
 import os 
 FileList=[] 
 FileNames=os.listdir(FindPath) 
 if (len(FileNames)>0): 
  for fn in FileNames: 
   if (len(FlagStr)>0): 
    #����ָ�����͵��ļ��� 
    if (IsSubString(FlagStr,fn)): 
     fullfilename=os.path.join(FindPath,fn) 
     FileList.append(fullfilename)
   else: 
    #Ĭ��ֱ�ӷ��������ļ��� 
    fullfilename=os.path.join(FindPath,fn) 
    FileList.append(fullfilename) 
 #���ļ������� 
 if (len(FileList)>0): 
  FileList.sort() 
 return FileList

aa = GetFileList('C:\Users\laoer123\Desktop','gz')

for i in range (0,127):
    print aa[i]
    un_gz(aa[i])

'''
for i in range (001,126):
        url = 'C:/Users/laoer123/Desktop/'+'.gz000'+str(i)+'.gz'
        print url
#	un_gz(url)
'''
