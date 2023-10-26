a=[0]*1005
a[0]=a[1]=1
for i in range(2,1005):
    if a[i]==0:
        for j in range(i*i,1005,i):
            a[j]=1



n=int(input())
lis=[int(x) for x in input().split()]
b=[0]*1005
c=[]
for i in range(0,n):
    if a[lis[i]]==0:
        b[i]=1
        c.append(lis[i])
c.sort()
res=0
for i in range(0,n):
    if b[i]==0:
        print(lis[i],end=' ')
    else:
        print(c[res],end=' ')
        res+=1