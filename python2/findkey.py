s = ""
s0 = "Aabycimergj"
s1 = ""
s2 = "%+$-4-8+7=?"
s3 = ""
s4 = ""

for i in s0:
    i = chr(ord(i)+5)
    #print i
    s1 += i
#print s1


for i in range(len(s1)):
    s3 += chr(ord(s1[i]) ^ ord(s2[i]))
#print s3

for i in s3:
    i = chr(ord(i)-5)
    #print i
    s4 += i
print s4

s = s4[::-1]
print s
