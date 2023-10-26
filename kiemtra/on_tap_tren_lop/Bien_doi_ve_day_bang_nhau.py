n = int(input())

a = [ int(x) for x in input().split()]

s = 1e9+7

for i in a:
    ans=0
    for j in a:
        ans += abs(i-j)

    if ans < s:
        s=ans
        p=i
print(s,p)