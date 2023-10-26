t = int(input())

def sum_digit(n):
    digit=0
    while n>0:
        digit += (n%10)
        n //= 10
    return digit
while t>0:
    n = int(input())
    a=list(map(int,input().split()))
    a.sort(key=lambda x: (sum_digit(x),x) )
    for i in a:
        print(i,end=' ')
    print()
    t -= 1