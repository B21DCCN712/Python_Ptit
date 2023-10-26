n=int(input())
a=[]
b=[]
s=0
for i in range(n):
    x=list(map(int,input().split()))
    a.append(x)
    b.append(sum(x))
    s += b[-1]
s = s/(2*n-2)
for i in b:
    print(int((i-s) / (n-2)) , end=' ')
        
