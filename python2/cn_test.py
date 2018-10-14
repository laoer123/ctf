# coding=utf-8

'''
a = "这是一个中文测试"
b = a.encode('gbk')
print b.decode('gbk')


age = 3
if age >= 18:
	print 'adult'
elif age >= 6:
	print 'teenager'
else:
	print 'kid'

birth = input('birth:')
if ord(birth) < 2000:
        print '00前'
else:
        print '00后'
'''

a = "这是一个中文测试"
print a
height = 1.75
weight = 80.5
bmi = weight/(height*height)
#print bmi

if bmi < 18.5:
        print '过轻'
elif bmi >= 18.5 and bmi <= 25:
        print '正常'
elif bmi >= 25 and bmi <= 28:
        print '过重'
elif bmi >=28 and bmi <=32:
        print '肥胖'
else:
        print '严重肥胖'

