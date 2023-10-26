s=input()
a={}
k=int(input())
Max=-1
for i in range(0,len(s),2):
    x=int(s[i:i+2])
    if x in a: a[x]+=1
    elif x>=10: a[x]=1
    if x>10:
        Max = max(Max,a[x])
if k>Max:print("NOT FOUND")

else:
    for i in sorted(a):
        if a[i]>=k:
            print(f"{i} {a[i]}")