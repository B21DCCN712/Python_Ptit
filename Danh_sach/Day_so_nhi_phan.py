n=int(input())
a=list(map(int,input().split()))

res=0
for i in range(1,n):
    if a[i] + a[i-1]==1:
        res += 1
print(res)