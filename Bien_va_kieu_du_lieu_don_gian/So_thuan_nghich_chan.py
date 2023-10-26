def sothuannghichchan(n):
    n=str(n)
    if len(n) % 2 == 1 :
        return 0
    if n != n[::-1]:
        return 0
    for i in n:
        if i != '0' and i != '4' and i != '6' and i != '2' and i != '8':
            return 0
    return 1
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(22,n,22):
        if sothuannghichchan(i):
            print(i,end=' ')
    print()