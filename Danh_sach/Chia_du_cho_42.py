a=[]
while len(a)<10:
    a += list(map(int,input().split()))

x= set()

for i in a:
    x.add(i % 42)
print(len(x))