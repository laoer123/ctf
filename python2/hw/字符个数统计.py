s = raw_input()
l = list(s)
#print l
result = []
count = 0
for i in l:
    if i not in result:
        result.append(i)
        count += 1
print count
