n,m=map(int,input().split())

a=[int(x) for x in input().split()]

x={}
s,z,y=0,0,0
for i in a:
    if i not in x: x[i]=1
    else: x[i]+=1
    s=max(s,x[i])
for i in range(1,m+1):
    if i in x and x[i]!=s and x[i]>y:
        y=x[i]
        z=i
if z==0:
    print("NONE")
else:
    print(z)