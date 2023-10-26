t = int(input())

def sodep(s):
    for i in range(2,len(s)):
        if s[i] != s[i-2]:
            return False
    return True
while t>0:
    s = input()
    if sodep(s):
        print("YES")
    else:
        print("NO")
    t -=1
