#-* coding: utf-8 -*
import hashlib
import base64
import itertools as its
import os
import sys
reload(sys)
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
specialChars = '~!@#$%^&*()_+{}|:"<>?`-=[]\;\',./'
numbers = "1234567890"
words = chars + specialChars + numbers
 
def get_FileSize(filePath):
    filePath = unicode(filePath,'utf8')
    if os.path.isfile(filePath):
        fsize = os.path.getsize(filePath)
        fsize = fsize / float(1024 * 1024)
        return round(fsize, 2)
    return 0
 
def MD5(s):
    m2 = hashlib.md5()
    m2.update(s)
    return m2.hexdigest()
def write2File(p,s):
    f = open(p, 'a')
    f.write(s)
    f.close()
filePath = 'D:\\'
 
def createHash(cs,lenth):
    r =its.product(cs,repeat=lenth)
    fileIndex = 0
    for i in r:
        str_plaintext = ''.join(i) #明文
        str_md5_32 = MD5(str_plaintext)
        str_md5_16 = str_md5_32[8:24]
 
        str_md5_32_md5_32 = MD5(str_md5_32)
        str_md5_32_md5_16 = str_md5_32_md5_32[8:24]
 
        str_md5_16_md5_32 = MD5(str_md5_16)
        str_md5_16_md5_16 = str_md5_16_md5_32[8:24]
 
 
        str_md5_16_base64 = base64.b64encode(str_md5_16)
        str_md5_16_base64_md5_32 = MD5(str_md5_16_base64)
        str_md5_16_base64_md5_16 = str_md5_16_base64_md5_32[8:24]
 
        str_md5_32_base64 = base64.b64encode(str_md5_32)
        str_md5_32_base64_md5_32 = MD5(str_md5_32_base64)
        str_md5_32_base64_md5_16 = str_md5_32_base64_md5_32[8:24]
 
        # Base64
        str64 = base64.b64encode(str_plaintext)
        str64_md5_32 = MD5(str64)
        str64_md5_16 = str64_md5_32[8:24]
 
        str64_md5_32_MD5_32 = MD5(str64_md5_32)
        str64_md5_32_MD5_16 = str64_md5_32_MD5_32[8:24]
 
        str64_md5_16_MD5_32 = MD5(str64_md5_16)
        str64_md5_16_MD5_16 = str64_md5_16_MD5_32[8:24]
 
 
        str64_md5_16_base64 = base64.b64encode(str64_md5_16)
        str64_md5_16_base64_md5_32 = MD5(str64_md5_16_base64)
        str64_md5_16_base64_md5_16 = str64_md5_16_base64_md5_32[8:24]
 
        str64_md5_32_base64 = base64.b64encode(str64_md5_32)
        str64_md5_32_base64_md5_32 = MD5(str64_md5_32_base64)
        str64_md5_32_base64_md5_16 = str64_md5_32_base64_md5_32[8:24]
 
        '''
        Save 2 File
        '''
        fileName = str(lenth) + '_' + str(fileIndex) + '.txt'
 
        fileSize = get_FileSize(filePath + fileName)
        if fileSize > 10 * 1024:# 10G
            fileIndex = fileIndex + 1
            fileName = str(lenth) + '_' + str(fileIndex) + '.txt'
 
        values = \
            str_plaintext + \
            ' ' + str_md5_32 + \
            ' ' + str_md5_16 + \
            ' ' + str_md5_32_md5_32 + \
            ' ' + str_md5_32_md5_16 + \
            ' ' + str_md5_16_md5_32 + \
            ' ' + str_md5_16_md5_16 + \
            ' ' + str_md5_16_base64 + \
            ' ' + str_md5_16_base64_md5_32 + \
            ' ' + str_md5_16_base64_md5_16 + \
            ' ' + str_md5_32_base64 + \
            ' ' + str_md5_32_base64_md5_32 + \
            ' ' + str_md5_32_base64_md5_16 + \
            ' ' + str64 + \
            ' ' + str64_md5_32 + \
            ' ' + str64_md5_16 + \
            ' ' + str64_md5_32_MD5_32 + \
            ' ' + str64_md5_32_MD5_16 + \
            ' ' + str64_md5_16_MD5_32 + \
            ' ' + str64_md5_16_MD5_16 + \
            ' ' + str64_md5_16_base64 + \
            ' ' + str64_md5_16_base64_md5_32 + \
            ' ' + str64_md5_16_base64_md5_16 + \
            ' ' + str64_md5_32_base64 + \
            ' ' + str64_md5_32_base64_md5_32 + \
            ' ' + str64_md5_32_base64_md5_16
 
        write2File(filePath + fileName, values+'\n')
createHash(words,4)
 
