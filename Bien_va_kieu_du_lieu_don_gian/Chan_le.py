t = int(input())

while t>0:
    s = input()
    res=0
    check=1
    for i in range(0,len(s)-1):
        if abs(int(s[i])-int(s[i+1]) ) != 2:
            check=0
            break
        res += int(s[i])
    res += int(s[len(s)-1])
    if res % 10 != 0:
        check=0
    if check==1:
        print("YES")
    else:
        print("NO")
    t = t-1