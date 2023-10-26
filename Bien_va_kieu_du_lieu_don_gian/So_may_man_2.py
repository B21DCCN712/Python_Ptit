t = int(input())
for i in range(1,t+1):
    n = input()
    check=1
    for i in n:
        if i != '4' and i != '7' :
            check=-1
    if check==1 : print("YES")
    else : print("NO")