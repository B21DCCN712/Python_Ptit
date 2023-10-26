mod = 1e9+7

def pow(a,b):
    if b==0 : return 1
    x = pow(a,int(b/2))
    x = (x*x) % mod
    if b % 2 == 1:
        x*=a
    return x % mod

def fun(n,k):
    if k <=1:
        return k
    x=0
    while ( k >> x) ^ 1:
        x+=1
    return (pow(n,x) + fun(n,k^(1<<x))) % mod

t = int(input())

while t>0:
    n,k = map(int , input().split())
    print(int(fun(n,k)))
    t -=1