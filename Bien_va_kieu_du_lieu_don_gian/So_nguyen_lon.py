t = int(input())

def gcd(a,b):
    if b==0 :
        return a
    return gcd(b,a%b)
while t>0:
    a=input()
    b=input()
    print(gcd(int(a),int(b)))
    t -=1