import sys
def reverse(sen):
    sen1 = sen.split(' ')
    sen2 = sen1[::-1]
    print " ".join(sen2)

reverse(raw_input())

