t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    b=[]
    dp=[1]*(n+5)
    for i in range(n):
        x,y=map(float,input().split())
        a.append(x)
        b.append(y)
    res=1
    for i in range(0,n):
        for j in range(0,i):
            if a[i]>a[j] and b[i]<b[j]:
                dp[i]=max(dp[i],dp[j]+1)
                res=max(res,dp[i])
    print(res)
