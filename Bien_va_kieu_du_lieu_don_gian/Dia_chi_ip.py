t=int(input())
while t>0:
    s=input()
    a=s.split(".")
    check=1
    for i in a:
        if int(i)>255 or int(i)<0 or not i.isdigit():
            check=-1
            break
    if len(a) !=4:
        check=-1
    if check==1:
        print("YES")
    else:
        print("NO")
    t-=1