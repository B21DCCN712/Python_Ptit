t = int(input())

while t>0:
    n = int(input())
    a=list(map(int,input().split()))
    mymap={}
    fmax=1
    num = 1e7
    for i in a:
        if i not in mymap:
            mymap[i]=1
        else :
            mymap[i] += 1
    fmax = max(mymap.values())
    for i,j in mymap.items():
        if j == fmax:
            num = min(num,i)
    if fmax <= int(n/2):
        print("NO")
    else:
        print(num)
    t -= 1
