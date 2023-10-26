t = int(input())

while t>0:
    s = input()
    kt=1
    for i in range(0, len(s)-1):
        if int(s[i]) > int(s[i+1]):
            kt=0
            break
    if kt == 1:
        print("YES")
    else:
        print("NO")
    t -= 1