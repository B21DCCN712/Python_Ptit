n=int(input())
a=[]
while True:
    A=[int(x) for x in input().split()]
    a+=A
    if len(a)==n : break
x=[]
y=[]
z=[0]*n
for i in range(n):
    if a[i]%2 ==0:
        x.append(a[i])
        z[i]=1
    else:
        y.append(a[i])
x.sort()
y.sort(reverse=True)
i,j=0,0
for k in range(n):
    if z[k]==1:
        print(x[i],end=" ")
        i+=1
    else:
        print(y[j],end=" ")
        j+=1
# print(x)
# print(y)
