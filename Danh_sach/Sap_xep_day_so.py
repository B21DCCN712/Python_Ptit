t=int(input())

while t>0:
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    Max=max(a)
    b=[]
    c=[]
    for i in range(n):
        if a[i]==Max:
            a.insert(i,k)
            break
    for i in a:
        if i <0 : b.append(i)
        else:c.append(i)
    for i in b:print(i,end=" ")
    for i in c: print(i,end=" ")
    print()
    t-=1