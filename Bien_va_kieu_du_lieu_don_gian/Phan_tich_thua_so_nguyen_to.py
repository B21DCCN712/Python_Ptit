t = int(input())

while t>0:
    n = int(input())
    i=2
    s="1"
    while n>1:
        if n % i == 0:
            x=0
            while n % i==0:
                x += 1
                n /=i
            s = s + " * "+  str(i) + "^" + str(x)
        i += 1
    print(s)
    t -=1