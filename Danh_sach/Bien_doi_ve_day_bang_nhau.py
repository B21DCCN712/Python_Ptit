n=int(input())
a=[int(x) for x in input().split()]
res=10**9
for i in a:
    s=0
    for j in a:
        s+=abs(i-j)
    if res > s:
        res=s
        p=i
print(res, p)