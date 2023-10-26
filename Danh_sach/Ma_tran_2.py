n=int(input())

a = []
for i in range(n):
   a.append(list(map(int,input().split())))
nuatren,nuaduoi=0,0
for i in range(n):
    for j in range(n):
        if j<n-i-1:
            nuatren += a[i][j]
        elif j>n-i-1:
            nuaduoi += a[i][j]
k=int(input())
x=abs(nuaduoi-nuatren)
if x<=k:
    print("YES")
else:
    print("NO")
print(x)
    