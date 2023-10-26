s=input()
a={}

for i in range(0,len(s),2):
    x=int(s[i:i+2])
    if x not in a and x>10: a[x]=1
for i in sorted(a):
    print(i,end=' ')