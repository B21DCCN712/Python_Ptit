import math
a =[0] * 10000005

def sang():
    a[0]=a[1]=1
    for i in range(2,math.sqrt(10000005)):
        if a[i]==0:
            for j in range(i*i,10000005,i):
                a[j]=1

sang()
t=int(input())

while t> 0:
    n = int(input())
    res=0
    for i in range(2,n-6):
        if a[i]==0 and a[i+6]==0 and( a[i+2]==0 or a[i+4]==0):
            res +=1
    print(res)
    t -=1