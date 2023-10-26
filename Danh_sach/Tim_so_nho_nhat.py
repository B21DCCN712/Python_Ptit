n = int(input())

while n > 0:
    s = input()
    s += "*"
    res = float('inf')
    x = 0
    l = len(s)
    for i in range(l):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
        else:
            if x != 0:
                res = min(res, x)
                x = 0
    print(res)
    n -= 1
