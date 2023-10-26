t = int(input())
while t>0:
    s=input()
    idx=len(s) // 2
    s1=s[:idx]
    s2=s[idx:]
    sum1=0
    sum2=0
    for i in range(0,idx):
        sum1 += ord(s1[i])-ord('A')
        sum1 += ord(s2[i])-ord('A')
    for i in range(0,idx):
        x1= ( ord(s1[i])-ord('A') + sum1 ) % 26
        x2= ( ord(s2[i])-ord('A') + sum2 ) % 26
        x1=(x1+x2)%26
        print(chr(x1+65),end="")
    print()
    t-=1
