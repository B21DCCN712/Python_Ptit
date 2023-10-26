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
    l = len(s)
    if nguyento(l)==0:
        return 0
    prime=0
    not_prime=0
    for i in s:
        if nguyento(int(i)) == 1:
            prime += 1
        else : not_prime += 1
    if prime <= not_prime:
        return 0
    return 1
    
            
while t>0:
    s = input()
    if check(s)==1:
          print("YES")
    else:
     print("NO")
    t -= 1
