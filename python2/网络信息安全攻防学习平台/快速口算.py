#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
# Date: 2014/11/25
# Created by ���Եȴ�
# ���� http://www.waitalone.cn/
import re

try:
    import requests
except ImportError:
    raise SystemExit('\n[!] requestsģ�鵼�����,��ִ��pip install requests��װ!')

print '\n������Ϣ��ȫ����ѧϰƽ̨�ű��ص�2��\n'
s = requests.Session()
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
r = s.get(url)
res = unicode(r.content, 'utf-8').encode('gbk')
# print res

num = re.findall(re.compile(r'<br/>\s+(.*?)='), res)[0]
print '��ǰ��ȡ����Ҫ����ı��ʽ��������Ϊ:\n\n%s=%d\n' % (num, eval(num))

r = s.post(url, data={'v': eval(num)})
print re.findall(re.compile(r'<body>(.*?)</body>'), r.content)[0]
