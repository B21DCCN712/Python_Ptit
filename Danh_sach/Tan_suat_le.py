t=int(input())
while t>0:
    n=int(input())
    m={}
    a=[int(x) for x in input().split()]
    for i in a:
        if i not in m:
            m[i]=1
        else:
            m[i]+=1
    for i in m:
        if m[i]%2==1:
            print(i)
            break
    t-=1