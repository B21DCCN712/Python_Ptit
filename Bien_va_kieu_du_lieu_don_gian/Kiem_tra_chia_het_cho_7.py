t = int(input())

while t>0:
    n=int(input())
    x=1000
    while( x>0):
        if n % 7 == 0:
            break
        n = n + int( str(n)[::-1])
        x -=1
    if n % 7 == 0:
        print(n)
    else:
        print(-1)
    t -=1