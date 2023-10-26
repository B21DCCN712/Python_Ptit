import math
f=[0]*10001
def sang():
    f[0]=f[1]=1
    for i in range(2,int(math.sqrt(10001))):
        if f[i]==0:
            for i in range(i*i,10001,i):
                f[i]=1

sang()
a=[0]
for i in range(10001):
    if f[i]==0:
        a += [i]
p=0
n,k= [ int(x) for x in input().split() ]
for i in range(n+1):
    k += a[p]
    print(k,end=' ')
    p += 1