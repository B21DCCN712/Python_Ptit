t=int(input())
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    x=min(a)
    y=max(a)
    s=0
    for i in range(x,y+1):
        if i not in a:
            s+=1
    print(s)
    t-=1