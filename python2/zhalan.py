#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_ -*-

e = raw_input('fgal{cedcc2065db75d246e9a5d2fbc5ebf6e196b3dcf70dc228c6bc46787b40dc2838e27baa81c31be}')
elen = len(e)
field=[]
for i in range(0,elen):
      if(elen%i==0):
            field.append(i)
for f in field:
      b = elen / f
      result = {x:'' for x in range(b)}
      for i in range(elen):
            a = i % b;
           result.update({a:result[a] + e[i]})
      d = ''
      for i in range(b):
            d = d + result[i]
      print str(f)+'\t'+d
