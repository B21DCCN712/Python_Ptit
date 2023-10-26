def find(n,k):
    if k == 2**(n-1):
        return n
    elif k < 2**(n-1):
        return find(n-1,k)
    else :
        return find(n-1,k-2**(n-1))
t = int(input())
for i in range(t):
    n,k=[int(x) for x in input().split()]
    x = find(n,k)
    print(chr(64+x))
    
