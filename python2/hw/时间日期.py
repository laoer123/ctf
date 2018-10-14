import time
import datetime

'''
print time.gmtime()
print time.asctime(time.localtime())
#t = time.asctime(time.gmtime())
#print type(t)
#print time.asctime(time.gmtime())
#print '--------------------------'
#print time.localtime()
#print time.asctime(time.localtime())


#print time.clock()
#print time.sleep(1)
#print time.clock()

#print time.ctime()

#print time.localtime(time.gmtime())

d = date(2017,12,6)
#print date.weekday(d)
print date.isoweekday(d)


d1 = datetime.datetime.strptime('2017-12-06 17:41:20','%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('1984-04-22 17:41:20','%Y-%m-%d %H:%M:%S')
delta = d1 -d2
print d1
print d2
print delta
'''

now = datetime.datetime.now()
print now
delta = datetime.timedelta(days=3)
print delta
n_days = now + delta
print n_days.strftime('%Y-%m-%d %H:%M:%S')

d =  datetime.date(1984,4,22)
#print date.weekday(d)
print datetime.date.isoweekday(d)