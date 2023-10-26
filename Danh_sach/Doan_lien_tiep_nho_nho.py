t = int(input())

while t>0:
    n = int(input())
    a=list(map(int,input().split()))
    f=[]
    ans=[]
    for i in range(n):
        while len(ans) > 0 and a[i] >= a[ans[-1]]:
            ans.pop()
        if len(ans)==0:
            f.append(i+1)
        else:
            f.append(i-ans[-1])
        ans.append(i)
    for i in f:
        print(i,end=' ')
    print()
    t -= 1