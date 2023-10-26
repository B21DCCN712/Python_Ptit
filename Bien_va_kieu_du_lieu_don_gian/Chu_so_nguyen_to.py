import math
def prime(n):
    if n < 2:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1

def check(s):
    if not prime(len(str(s))) :
        return 0
    ans=0
    for i in s:
        if prime(int(i)):
            ans += 1
    if ans <= len(s)-ans:
        return 0
    return 1
t = int(input())
while t>0:
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1
