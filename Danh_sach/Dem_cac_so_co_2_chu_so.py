s=input()
a={}

for i in range(0,len(s),2):
    x=int(s[i:i+2])
    if x in a: a[x]+=1
    elif x>10: a[x]=1
for i in a:
    print(f"{i} {a[i]}")