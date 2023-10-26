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
    sum=0
    for i in range(0,len(s)):
        if i % 2 ==0:
            if int(s[i]) % 2 ==1:
                return 0
        else:
            if int(s[i]) % 2 == 0: return 0
        sum += int(s[i])
    if  nguyento(sum) == 0:
         return 0
    return 1
    
            
while t>0:
    s = input()
    if check(s)==1:
          print("YES")
    else:
     print("NO")
    t -= 1
