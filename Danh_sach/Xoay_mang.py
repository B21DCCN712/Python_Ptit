t = int(input())

while t>0 :
    n , k = map(int,input().split())
    list =[ int(i) for i in input().split()]
    for i in range(k,n):
        print(list[i],end=' ')
    for i in range(k):
        print(list[i],end=' ')
    print()
    t -= 1