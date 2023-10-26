def gcd(a,b):
    if b==0 :
        return a
    return gcd(b,a%b)

t = int(input())

while t > 0 :
    s1 = input()
    s2 = s1[::-1]
    s1 = int(s1)
    s2 = int(s2)
    if gcd(s1,s2) == 1:
        print("YES")
    else :
        print("NO")
    t -=1
