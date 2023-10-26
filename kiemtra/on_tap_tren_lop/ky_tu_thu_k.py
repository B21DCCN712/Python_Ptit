a = [0,1]

for i in range(1,27):
    a.append(a[i]*2)

for t in range(int(input())):
    n , k = map(int,input().split())
    for i in range(n,-1,-1):
        if k > a[i]:
            k -= a[i]
        if k == a[i]:
            print(chr(i+64))
            break
