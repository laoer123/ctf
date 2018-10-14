n=raw_input()
l=list(reversed(n))
print l
#l = list(set(n[::-1]))
result=[]
for i in l:
    if i not in result:
        result.append(i)
#print("".join(result))
#print (result)
print ("".join(result))