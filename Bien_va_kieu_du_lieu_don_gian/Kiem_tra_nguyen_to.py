import math
def isprime(n):
    if n<2:
        return 0
    for i in range(2, n):
        if n % i ==0:
            return 0
    return 1

t = int(input())

while t>0 :
    s=input()
    if len(s)<4:
        print("NO")
    else :
        s1=s[-4:]
        if isprime(int(s1)) == 1:
            print("YES")
        else :
            print("NO")
    #print(int(s1))
    t -=1