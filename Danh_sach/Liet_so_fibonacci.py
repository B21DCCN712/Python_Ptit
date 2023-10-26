a = [0]* 95
a[1]=a[2]=1
for i in range(3,93):
    a[i] = a[i-1]+a[i-2]

t = int(input())
while t>0:
    n,m = map(int,input().split())
    for i in range(n,m+1):
        print(a[i],end=' ')
    print()
    t -= 1