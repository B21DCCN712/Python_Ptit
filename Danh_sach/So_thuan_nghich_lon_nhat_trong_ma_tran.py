def thuannghich(n):
    if n<10 : return False
    if str(n) != str(n)[::-1]: return False
    return True

n,k=map(int,input().split())

a = [[0]] * n

for i in range(0,n):
    a[i] = [int(x) for x in input().split()]
check=-1
res=0
for i in range(n):
    for j in range(k):
        if thuannghich(a[i][j]):
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