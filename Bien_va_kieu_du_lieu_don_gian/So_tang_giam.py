t = int(input())
# 12345
def check(s):
    if len(s) < 3:
        return False
    l=0 
    r=len(s)-1
    while s[l] < s[l+1] and l+1 < len(s) : l += 1
    while s[r] < s[r-1]  and r-1 >=0: r -= 1
    if l != r:
        return False
    else :
        return True
while t>0:
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
    t -= 1
