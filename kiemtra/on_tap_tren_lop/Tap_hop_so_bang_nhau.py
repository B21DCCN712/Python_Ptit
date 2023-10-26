n,m=map(int,input().split())
a=set()
b=set()
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in x:
    a.add(i)
for i in y:
    b.add(i)

if a==b:
    print("YES")
else:
    print("NO")