t = int(input())

while t>0:
    s = input()
    n = len(s)
    res=""
    nho=0
    if n==1:
        print(s)
    else:
        for i in range(n-1,0,-1):
            if int(s[i]) + nho < 5:
                res = "0" + res
                nho=0
            else:
                nho=1
                res = "0" + res
        if nho + int(s[0]) >= 10 :
            res = "10" + res
        else :
            res = str(int(s[0]) + nho) + res
            
        print(res)
    t -= 1