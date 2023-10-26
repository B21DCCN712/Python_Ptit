
t = int(input())
while t>0:
    s = input()
    res=0
    for i in s:
        res += int(i)
    res = str(res)
    if res == res[::-1] and len(res)>1:
         print("YES")
    else:
         print("NO")
    t -= 1