def nguyento(n):
    if( n < 2) :
        return 0
    else:
        for i in range(2,n):
            if( n % i ==0):
                    return 0 
    return 1

def gcd(a,b):
    if b == 0 : return a
    return gcd(b,a%b)

t= int(input())
for i in range(0,t):
    res=0
    n=int(input())
    for j in range ( 1, n):
        if gcd(j,n)==1 : res+=1

    if nguyento(res) == 1:
        print("YES")
    else :
        print("NO")

