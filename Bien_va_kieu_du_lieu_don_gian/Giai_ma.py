t = int(input())

while t>0 :
    s = input()
    res=""
    for i in range(0,len(s)) :
        if s[i]>='1' and s[i] <='9':
            idx=s[i-1]
            idx *= int(s[i])
            res += idx
    print(res)
    t -=1