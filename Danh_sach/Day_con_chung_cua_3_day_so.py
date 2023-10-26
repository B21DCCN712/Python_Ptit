t=int(input())
while t>0:
    n,m,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    x,y,z,check=0,0,0,0
    while x<n and y<m and z<k:
        if a[x]==b[y] and b[y]==c[z]:
            print(a[x],end=' ')
            check=1
            x+=1
            y+=1
            z+=1
        elif a[x]<b[y]:x+=1
        elif b[y]<c[z]:y+=1
        elif c[z]<a[x]:z+=1
    if check==0:
        print("NO")
    else:
        print()
    t-=1