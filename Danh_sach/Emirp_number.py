def is_prime(n):
    if n==2 : return 1
    if n < 2 or n % 2 ==0: 
        return 0
    i=3
    while i*i <=n:
        if n % i ==0 : return 0
        i+=2
    return 1

def perfect_prime(n):
    if not is_prime(n):
        return 0
    n = str(n)
    if n == n[::-1]:
        return 0
    if not is_prime(int(n[::-1])):
        return 0
    return 1
t = int(input())
while t>0:
    n = int(input())
    for i in range(2,n):
        k = int(str(i)[::-1])
        if k > i and k < n and perfect_prime(i) and perfect_prime(k):
            print(i,k,end=' ')
    print()
    t -= 1


