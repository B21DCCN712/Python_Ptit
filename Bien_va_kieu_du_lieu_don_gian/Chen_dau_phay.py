s = input()
res=""
n=len(s)
for i in range(0,n):
    res += s[i]
    if (n-i-1)%3==0 and i!=n-1:
        res += ','
print(res)
