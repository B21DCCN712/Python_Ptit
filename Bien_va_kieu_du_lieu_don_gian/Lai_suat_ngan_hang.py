def year(n, m, x):
    years = 0
    while n < m:
        interest = n * x / 100
        n += interest
        years += 1
    return years

t = int(input())

for i in range(t):
    input_str = input()  # Đọc chuỗi đầu vào chứa 3 số double
    n, x, m = map(float, input_str.split())  # Tách chuỗi thành 3 số và chuyển thành float
    print(year(n, m, x))
