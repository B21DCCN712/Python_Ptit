
def Try(res,n):
    if n == 1 :
        return res
    else:
        if n % 2 == 0 :
            Try(res+1,n//2)
        else:
            Try(res+1,n*3+1)
while True:
    n = int(input())
    if n == 0 :
        break
    a=set()
    a.add(n)
    while n!= 1:
        if n % 2 == 1 :
            n=n*3+1
        else:
            n /= 2
        a.add(n)
    print(len(a))
