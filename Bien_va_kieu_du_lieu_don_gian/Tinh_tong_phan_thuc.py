t = int(input())

while t > 0:
    n = int(input())
    if n % 2 == 0:
        res = 0
        for i in range(2, n + 1, 2):
            res += 1 / i
        formatted_result = "{:.6f}".format(res)
        print(formatted_result)
    else:
        res = 0
        for i in range(1, n + 1, 2):
            res += 1 / i
        formatted_result = "{:.6f}".format(res)
        print(formatted_result)
    t -= 1
