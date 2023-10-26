def nguyento(n):
    if( n < 2) :
        return 0
    else:
        for i in range(2,n):
            if( n % i ==0):
                    return 0 
    return 1

t = int(input())
while t>0:
    s = input()
    res=0
    for i in s:
        res += int(i)
    if nguyento(res):
         print("YES")
    else:
         print("NO")
    t -= 1