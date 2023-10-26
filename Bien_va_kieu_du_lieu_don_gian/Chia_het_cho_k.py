a, k, n = map(int, input().split())

b = []

n -= a
i = k -(a%k)

while i <= n:
    b.append(i)
    i += k
if len(b)==0:
    print(-1)
else :
    for i in b :
        print(i,end=' ')