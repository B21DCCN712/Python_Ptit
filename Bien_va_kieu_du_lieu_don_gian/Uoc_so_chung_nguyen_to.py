t = int(input())

def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)
def nguyento(n):
    if( n < 2) :
        return 0
    else:
        for i in range(2,int(n ** 0.5)+1):
            if( n % i ==0):
                    return 0 
    return 1
def check(n):
    res=0
    while n > 0:
          res += n%10
          n = n // 10
    if nguyento(res) == 1: return 1
    else :return 0
while t>0 :
    a,b = map(int , input().split())
    c = gcd(a,b)
    if check(c)==1: print("YES")
    else: print("NO")
    t=t-1