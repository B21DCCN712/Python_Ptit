import math
n = int(input())
a=list(map(int,input().split()))

def prime(n):
    if n < 2:
        return False
    if n==2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i=5
    while i * i <= n:
        if n % i ==0 or n % (i+2)==0 :
            return False
        i += 6
    return True
d=[0] * 1000005
for i in a:
    d[i] += 1
for i in a:
    if d[i]>0 and prime(i):
        print(i,d[i])
        d[i]=0