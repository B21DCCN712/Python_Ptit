import bisect
mymap={}
f=[0]*11000
f[0]=1
a2,a3,a5=0,0,0
for i in range(1,11000):
    f[i]=min( f[a2]*2 , min(f[a3]*3,f[a5]*5))
    if f[i]==f[a2]*2:a2 += 1
    if f[i]==f[a3]*3:a3 += 1
    if f[i]==f[a5]*5:a5 += 1
t=int(input())

def binSearch(l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if f[mid] == x:
            return mid +1
        if f[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1

while t>0:
    n=int(input())
    idx = binSearch(0,len(f)-1,n)
    if idx == -1:
        print("Not in sequence")
    else:
        print(idx)
    t -=1


