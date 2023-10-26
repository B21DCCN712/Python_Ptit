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
    s=s[-4:]
    if nguyento(int(s))==1:
        return 1
    return 0
    
            
while t>0:
    s = input()
    if check(s)==1:
          print("YES")
    else:
     print("NO")
    t -= 1
