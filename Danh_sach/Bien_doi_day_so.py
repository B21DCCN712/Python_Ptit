import math
while True:
    a,b,c,d=map(int,input().split())
    if a==b and b==c and c==d and d==0:
        break
    res=0
    while True:
        if a==b and b==c and c==d:
            break
        x = d-a
        a= abs(a-b)
        b= abs(b-c)
        c= abs(c-d)
        d= abs(x)
        res += 1
    print(res)
# 1 3 5 9
# 2 2 4 8
# 0 2 4 6
# 2 2 2 6
# 0 0 4 4
# 0 4 0 4
# 4 4 4 4