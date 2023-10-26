n= int(input())
a = list(map(int,input().split()))
a.sort()
i=1
while True:
    if i not in a:
        print(i)
        break
    i += 1