t = int(input())

while t>0:
    n,p=map(int,input().split())
    res=0
    for i in range(1,n+1):
        if i % p == 0:
            while i % p == 0:
                res += 1
                i /= p
    print(res)
    t -= 1