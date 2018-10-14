# -*- coding:utf-8 -*-
def maopao(l):
    index = 0
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
                index += 1
    return index

def choice(l):
    index = 0
    for i in range(0,len(l)):
        min = i
        for j in range(i+1,len(l)):
            if l[min] > l[j]:
                min = j
        l[min],l[j] = l[j],l[min]
        index += 1
    return index

def insert_sort(lists):
    # 插入排序
    index = 0
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return index

def insert(l):
    index = 0
    count = len(l)
    for i in range(1,count):
        key = l[i]
        j = i - 1
        while j>= 0 :
            if l[j] > key:
                l[j+1] = l[j]
                l[j] = key
                index += 1
            j -= 1
    return index


while True:
    try:
        a = raw_input().split(' ')
        b = []
        for i in a:
            b.append(int(i))
        #print maopao(b)
        #print choice(b)
        print insert(b)
    except:
        break