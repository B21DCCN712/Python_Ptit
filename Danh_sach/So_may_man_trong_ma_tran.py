n,k=map(int,input().split())

a = [[0]] * n
Min,Max=1000000,0
for i in range(0,n):
    a[i] = [int(x) for x in input().split()]
    Min=min(Min,min(a[i]))
    Max=max(Max,max(a[i]))
res=Max-Min
check=-1
for i in range(n):
    for j in range(k):
        if a[i][j]==res:
            check=1
            break
if check==-1:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(k):
            if a[i][j]==res:
                check=1
                print(f"Vi tri [{i}][{j}]")