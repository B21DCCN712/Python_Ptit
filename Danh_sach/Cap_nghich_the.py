n=int(input())
res=0
a=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            res+=1
print(res)