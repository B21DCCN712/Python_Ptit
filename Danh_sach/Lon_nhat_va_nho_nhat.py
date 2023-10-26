while True:
    n=int(input())
    if n==0:break
    a=[]
    for i in range(n):
        x=int(input())
        a.append(x)
    x=min(a)
    y=max(a)
    if x==y:print("BANG NHAU")
    else:print(f"{x} {y}")