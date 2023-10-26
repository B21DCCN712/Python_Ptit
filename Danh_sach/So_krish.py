def giaithua(n):
    if n ==0 : return 1
    x=1
    for i in range(1,n+1):
        x *= i
    return x

t = int(input())
while t> 0:
    s = input()
    res=0
    for i in s:
        res += giaithua(int(i))
    if res == int(s):
        print("Yes")
    else:
        print("No")
    t -=1