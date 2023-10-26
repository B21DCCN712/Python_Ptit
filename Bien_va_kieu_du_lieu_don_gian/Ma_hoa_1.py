t = int(input())

while t>0:
    s = input()
    n=len(s)
    res=""
    ans=1
    for i in range(1,n):
        if s[i] != s[i-1]:
            res = res +str(ans) + s[i-1]
            ans =1
        else : ans +=1
    res = res +str(ans) + s[n-1]
    print(res)
    t -=1