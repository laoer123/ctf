# -*- coding: utf-8 -*-
import xlwt
import time
import xlrd
import urllib
import re
from xlutils.copy import copy

now = time.strftime("%Y.%m.%d")
workbook = xlrd.open_workbook(u'E:/stock/chicang/2018.05.05.xls')
rs = workbook.sheet_by_index(0)
wb = copy(workbook)
ws = wb.get_sheet(0)
# ws_tongji = wb.get_sheet(1)
ncols = rs.ncols
nrows = rs.nrows

ws.write(0, ncols, now)
# ws1.write(0, ncols, now)


for i in xrange(1,13):
    rowValues= rs.row_values(i,1,2)
    for item in rowValues:
        url = "https://gupiao.baidu.com/stock/" + item + ".html"

        content = urllib.urlopen(url).read()

        res_tr = r'(div class="price s-up ">|<div class="price s-down ">|<div class="price s-stop ">)(.*?)</div>'
        m_tr = re.findall(res_tr, content, re.S | re.M)
        for line in m_tr:
            res_th = r'<strong  class="_close">(.*?)</strong>'
            m_th = re.findall(res_th, str(line), re.S | re.M)
            # for mm in m_th:
            #     print item,unicode(mm, 'utf-8'),
            ws.write(i, ncols, m_th)
        # ws_tongji.write(i,ncols,m_th)

for i in xrange(0, nrows):
    gushu = rs.cell(i,4)
    ws.write(i, ncols + 1, gushu.value)

    # print type(gushu.value)
    # print type(rs.cell(i,3).value)

# ws.write(0, ncols + 2, "市值")

# for i in xrange(1, nrows):
#     ws.write(i, ncols + 2, rs.cell(i,3).value * rs.cell(i,4).value)


wb.save("E:/stock/chicang/"+now+".xls")

# newfile = "E:/stock/chicang/"+now+".xls"
# workbook1 = xlrd.open_workbook(newfile)
# worksheet1 = workbook1.sheets()[0]
# num_rows = worksheet1.nrows
# for curr_row in range(1:13):
#     row = worksheet1.row_values(curr_row)
#     worksheet1.
# print('row%s is %s' %(curr_row,row))


