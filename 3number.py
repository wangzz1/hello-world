#有四个数字1,2,3,4能组成多少个互不
#相同且无重复数字的三位数，各是多少？

a = [1,2,3,4]

for i in a:
    for j in a:
        for k in a:
            if i!= j != k:
                print(i,end='',j,end='',k,end='')
            


    
