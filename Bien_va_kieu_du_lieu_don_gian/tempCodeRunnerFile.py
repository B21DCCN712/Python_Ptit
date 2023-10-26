t=int(input())
while t>0:
    s=input()
    a=s.split(".")
    if len(a)<4:
        print("NO")
        continue
    check=1
    for i in a:
        if not i.isdigit() or int(i)>255 or int(i)<0 :
            check=-1
            break
    if check==1:
        print("YES")
    else:
        print("NO")
    t-=1