def base_8(s):
    return 4*int(s[0]) + 2 * int(s[1]) + 1 * int(s[2])

s=input()
while len(s) % 3 !=0:
    s='0'+s
res=''
for i in range(0,len(s),3):
    res += str(base_8(s[i:i+3]))
print(res)