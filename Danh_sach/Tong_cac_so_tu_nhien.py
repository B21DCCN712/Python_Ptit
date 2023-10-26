a=[]
def Try(n,sum,s):
    if sum==0: a.append(s.strip())
    for i in range(n,0,-1):
        if i<=sum: Try(i,sum-i,s+str(i)+" ")


t=int(input())
while t>0:
    n=int(input())
    Try(n,n,"")
    print(len(a))
    for i in a: print(f"({i})",end=' ')
    print()
    a.clear()
    t-=1