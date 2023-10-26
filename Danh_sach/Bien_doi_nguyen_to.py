import math
a=[0]*10005
a[0]=a[1]=1
for i in range(2,int(math.sqrt(10005))):
    if a[i]==0:
        for j in range(i*i,10005,i):
            a[j]=1

# for i in range(100):
#     if a[i]==0:
#         print(i,end=" ")

n=int(input())
list=[int(x) for x in input().split()]
res=0
for i in list:
    if a[i]==0:
        continue
    x,y=i,i
    while a[x]==1:x-=1
    while a[y]==1:y+=1
    res=max(res,min(i-x,y-i))
print(res)