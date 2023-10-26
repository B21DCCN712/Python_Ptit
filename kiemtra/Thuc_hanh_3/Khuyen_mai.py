n, k = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a = [[]]*n
for i in range(n):
    a[i] = [a1[i], a2[i]]
a.sort(key=lambda x: x[0]-x[1])
sum = 0
for i in range(k): sum+=a[i][0] #mua tối thiểu k món
i = k
while i<n and a[i][0] < a[i][1]: # mua thêm nếu trước rẻ hơn sau
    sum += a[i][0]
    i+=1
for j in range(i, n): sum += a[j][1] #mua nốt
print(sum)