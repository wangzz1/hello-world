#encoding = utf-8

#冒泡排序
a = [3,5,4,12,72,43,61,9,88,13]

for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
        
