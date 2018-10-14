#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
# Date: 2014/11/25
# Created by 独自等待
# 博客 http://www.waitalone.cn/
import re

try:
    import requests
except ImportError:
    raise SystemExit('\n[!] requests模块导入错误,请执行pip install requests安装!')

#print '\n网络信息安全攻防学习平台脚本关第2题\n'
s = requests.Session()
headers = {'Cookie': 'WC=9849127-36825-4TEkdwYlUYUsl1SC'}
url = 'http://www.wechall.net/challenge/training/programming1/index.php?action=request'
r = s.get(url)
res = unicode(r.content, 'utf-8').encode('gbk')
print res

#num = re.findall(re.compile(r'<br/>\s+(.*?)='), res)[0]
#print '当前获取到需要口算的表达式及计算结果为:\n\n%s=%d\n' % (num, eval(num))

#r = s.post(url, data={'v': eval(num)})
#print re.findall(re.compile(r'<body>(.*?)</body>'), r.content)[0]
