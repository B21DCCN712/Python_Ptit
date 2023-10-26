def count(a):
    n=len(a)
    left_max=[0]*n
    right_min=[0]*n
    left_max[0]=a[0]
    for i in range(1,n):
        left_max[i]=max(a[i],left_max[i-1])
    right_min[n-1]=a[n-1]
    for i in range(n-2,-1,-1):
        right_min[i] = min(a[i],right_min[i+1])
    res=0
    for i in range(1,n-1):
        if left_max[i-1] <= a[i] and a[i] < right_min[i+1]:
            res += 1
    if  left_max[0]<right_min[1]:
        res += 1
    if  left_max[n-1]<=right_min[n-1]:
        res += 1
    return res

t = int(input())
while t>0:
    n = int(input())
    a=list(map(int,input().split()))
    print(count(a))
    t -= 1

