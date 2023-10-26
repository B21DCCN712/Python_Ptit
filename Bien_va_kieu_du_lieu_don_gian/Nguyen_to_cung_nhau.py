def gcd(a,b):
    if b == 0 : 
        return a
    return gcd(b,a%b)

n , k = map(int,input().split())

ans=0

x = 10 ** (k-1)
y = 10 ** k 
for i in range(x,y):
    if gcd(i,n)==1:
        print(i,end=' ')
        ans +=1
        if ans % 10 ==0:
            print()