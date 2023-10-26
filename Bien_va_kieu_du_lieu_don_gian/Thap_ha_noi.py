def chuyen(n,a,b,c):
    if n==1:
        print(a+" -> "+c)
    else:
        chuyen(n-1,a,c,b)
        print(a+" -> "+c)
        chuyen(n-1,b,a,c)

n = int(input())
chuyen(n,'A','B','C') 