import math
x=10**7
a=[0] * x
def sang():
    a[0]=a[1]=1
    for i in range(2,x):
        if a[i]==0:
            a[i]=i
            for j in range(i*i,x,i):
                a[j]=i
sang()
res=0

t=int(input())
for i in range(t):
    n=int(input())
    while n!=1 :
        res += a[n]
        n  //= a[n]
print(res)