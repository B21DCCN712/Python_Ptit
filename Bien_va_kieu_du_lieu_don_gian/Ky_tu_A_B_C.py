n = int(input())
a=['A','B','C']

def check(s):
    demA=0
    demB=0
    demC=0
    for i in s:
        if i=='A':demA += 1
        elif i=='B':demB += 1
        else: demC += 1
    if demA <= demB and demB <= demC and demA >= 1:
        print(s)

def Try(i,s,n):
    if i==n:
        check(s)
    if i>n:
        return
    for x in a:
        Try(i+1,s+x,n)

for i in range(3,n+1):
    Try(0,'',i)