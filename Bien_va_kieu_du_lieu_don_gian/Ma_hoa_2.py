p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    ip = input()
    if ip == "0" :
        break
    k,s = ip.split()
    k = int(k)
    result=""
    for i in s:
        if i=='_':
            x=26
        elif i=='.':
            x=27
        else:
            x=ord(i)-ord('A')
        x = (x+k) % 28
        result = p[x] + result
    print(result)
