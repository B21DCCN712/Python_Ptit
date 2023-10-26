n = int(input())

a = list(map(float,input().split()))

x = max(a)
y = min(a)
dem=0
sum=0
for i in a:
    if i != x and i != y :
        sum += i
        dem += 1
print(round(sum/dem,2))