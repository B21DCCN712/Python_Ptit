s = input()
n = len(s)
f = [0] * 15
def Try(x):
    if len(x) == n:
        print(x)
    for i in range(0,n):
        if f[i]==0:
            f[i]=1
            Try(x+s[i])
            f[i]=0
Try("")

    