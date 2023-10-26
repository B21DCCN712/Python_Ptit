a=[0]*1000000
a[0]=a[1]=1
for i in range(2,1000000):
    if a[i]==0:
        for j in range(i*i,1000000,i):
            a[j]=1

n=int(input())
x=[int(x) for x in input().split()]
y={}
for i in x:
    y[i]=1
x=list(y)
n=len(x)
for i in range(1,n):
    x[i]=x[i-1]+x[i]
ok=0
for i in range(0,n):
    if a[x[i]]==0 and a[x[n-1]-x[i]]==0:
        print(i)
        ok=1
        break
if ok ==0:
    print("NOT FOUND")
