def gcd(a,b):
    if b == 0 : 
        return a
    return gcd(b,a%b)

l , r = map(int,input().split())

ans=0

for i in range(l,r+1):
    for j in range(i+1,r+1):
        for k in range(j+1,r+1):
            if gcd(i,j)==1 and gcd(i,k)==1 and gcd(j,k)==1:
                print('(' + str(i) + ', ' + str(j) + ', ' + str(k) +')')
    