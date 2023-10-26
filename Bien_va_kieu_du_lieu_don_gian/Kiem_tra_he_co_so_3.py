t = int(input())

while t>0:
    s = input()
    check=1
    for i in s:
        if i > '2' or i < '0':
            check=0
            break
    if check==1:
        print("YES")
    else:
        print("NO")
    t -= 1
