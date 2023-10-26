def cnt(s,d):
    if s=="Xe_con":
        if d==5:return 10000
        else:return 15000
    elif s=="Xe_khach":
        if d==29:return 50000
        else:return 70000
    else : return 20000

n=int(input())
m={}
for i in range(n):
    a=input().split()
    if a[3]=="IN":
        if a[4] not in m:
            m[a[4]] = cnt(a[1],int(a[2]))
        else:
            m[a[4]] += cnt(a[1],int(a[2]))

for i in m.keys():
    print(f"{i}: {m[i]}")