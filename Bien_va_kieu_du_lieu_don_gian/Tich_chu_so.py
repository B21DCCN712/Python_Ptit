t = int(input())
 
while t>0:
    s = input()
    x = 1
    for i in s:
        if int(i) != 0:
            x *= int(i)
    print(x)
    t -= 1
