

t = int(input())

def check(s):
    l = len(s)
    if l % 2 == 0 or s[0]==s[1] :
        return 0
    
    for i in range(2,len(s),2):
        if s[i] != s[i-2]:
            return 0
    return 1
    
            
while t>0:
    s = input()
    if check(s)== 1:
        print("YES")
    else:
        print("NO")
    t -= 1
