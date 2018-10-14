s0 = "v1G0F1CGGGA=215G7"
s1= ""

for i in range(0,len(s0)):
    s1 += chr(ord(s0[i]) ^ 5)

print s1[::-1]
