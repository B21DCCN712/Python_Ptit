def nguyento(n):
    if( n < 2) :
        return 0
    else:
        for i in range(2,n):
            if( n % i ==0):
                    return 0 
    return 1

t = int(input())

def check(s):
    tong=0
    tich=1
    le=0
    for i in range(0,len(s)):
        if i % 2 == 0:
            tong += int(s[i])
        else:
            if int(s[i]) != 0 :
                le += 1
                tich *= int(s[i])
    if le == 0 :
        tich=0
    print(f"{tong} {tich}")
    
            
while t>0:
    s = input()
    check(s)
    t -= 1
