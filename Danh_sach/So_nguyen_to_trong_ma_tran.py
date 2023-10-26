def prime(n):
    if n<2:return False
    for i in range(2,n):
        if n % i == 0 :return False
    return True


n,k=map(int,input().split())

a = [[0]] * n

for i in range(0,n):
    a[i] = [int(x) for x in input().split()]
check=-1
res=0
for i in range(n):
    for j in range(k):
        if prime(a[i][j]):
            check=1
            res=max(res,a[i][j])
if check==-1:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(k):
            if a[i][j]==res:
                print(f"Vi tri [{i}][{j}]")