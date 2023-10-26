n=int(input())
a=[int(x) for x in input().split()]
s,ans=min(a),0

def check(n):
    for i in a:
        if int(i/n) == int(i/(n+1)):
            return 0
    return 1

for i in range(s,0,-1):
    if check(i):
        for j in a:
            ans += int(j/(i+1))+1
        break
print(ans)