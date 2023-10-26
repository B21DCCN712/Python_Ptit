n = int(input())

while n > 0 :
    s=input()
    res=-1
    x=0
    s += "*"
    l=len(s)
    for i in range(0,l-1):
        if s[i].isdigit():
            x = x*10 + int(s[i])
        elif s[i].isalpha():
            res=max(res,x)
            x=0
    print(max(res,x))
    n=n-1