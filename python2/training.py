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

#print '\n������Ϣ��ȫ����ѧϰƽ̨�ű��ص�2��\n'
s = requests.Session()
headers = {'Cookie': 'WC=9849127-36825-4TEkdwYlUYUsl1SC'}
url = 'http://www.wechall.net/challenge/training/programming1/index.php?action=request'
r = s.get(url)
res = unicode(r.content, 'utf-8').encode('gbk')
print res

#num = re.findall(re.compile(r'<br/>\s+(.*?)='), res)[0]
#print '��ǰ��ȡ����Ҫ����ı��ʽ��������Ϊ:\n\n%s=%d\n' % (num, eval(num))

#r = s.post(url, data={'v': eval(num)})
#print re.findall(re.compile(r'<body>(.*?)</body>'), r.content)[0]
