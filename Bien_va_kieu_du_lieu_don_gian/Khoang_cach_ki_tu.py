t = int(input())

while t > 0:
    s1 = input()
    s2 = s1[::-1]
    n = len(s1)
    check = 1
    for i in range(1, n):
        diff1 = ord(s1[i]) - ord(s1[i-1])
        diff2 = ord(s2[i]) - ord(s2[i-1])
        if abs(diff1) != abs(diff2):
            check = -1
            break
    if check == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
