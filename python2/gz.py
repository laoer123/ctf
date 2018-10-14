import gzip
import os
def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    #获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    #创建gzip对象
    open(f_name, "w+").write(g_file.read())
    #gzip对象用read()打开后，写入open()建立的文件中。
    g_file.close()
    #关闭gzip对象

# -*- coding: utf-8 -*- 
#~ #------------------------------------------------------------------
#~ module:wlab 
#~ Filename:wgetfilelist.py 
#~ Function : 
#~ def IsSubString(SubStrList,Str) 
#~ def GetFileList(FindPath,FlagStr=[]): 
#~ 功能:读取指定目录下特定类型的文件名列表 
#~ Data: 2013-08-08,星期四 
#~ Author:吴徐平 
#~ Email:wxp07@qq.com 
#~ #------------------------------------------------------------------
#~ #------------------------------------------------------------------
def IsSubString(SubStrList,Str): 
 ''''' 
 #判断字符串Str是否包含序列SubStrList中的每一个子字符串 
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
 #获取目录中指定的文件名 
 #>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符 
 #>>>FileList=GetFileList(FindPath,FlagStr) # 
 '''
 import os 
 FileList=[] 
 FileNames=os.listdir(FindPath) 
 if (len(FileNames)>0): 
  for fn in FileNames: 
   if (len(FlagStr)>0): 
    #返回指定类型的文件名 
    if (IsSubString(FlagStr,fn)): 
     fullfilename=os.path.join(FindPath,fn) 
     FileList.append(fullfilename)
   else: 
    #默认直接返回所有文件名 
    fullfilename=os.path.join(FindPath,fn) 
    FileList.append(fullfilename) 
 #对文件名排序 
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
