n=int(input())
a=[int(x) for x in input().split()]
a.sort()

max1=max(a[0]*a[1],a[n-1]*a[n-2])
max2=max(a[0]*a[1]*a[n-1],a[n-1]*a[n-2]*a[n-3])
print(max(max1,max2))