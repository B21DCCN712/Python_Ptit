n=int(input())

a = []
for i in range(n):
   a.append(list(map(int,input().split())))
nuatren,nuaduoi=0,0
for i in range(n):
    for j in range(n):
        if i<j:
            nuatren += a[i][j]
        elif i>j:
            nuaduoi += a[i][j]
k=int(input())
x=abs(nuaduoi-nuatren)
if x<=k:
    print("YES")
else:
    print("NO")
print(x)
    