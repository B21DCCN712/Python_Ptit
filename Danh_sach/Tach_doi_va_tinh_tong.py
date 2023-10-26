def tinhtong(s):
    if int(s) < 10: return 
    else:
        l=len(s)
        n=str(int(s[:l//2]) + int(s[l//2:]))
        print(n)
        return tinhtong(n)

    
s=input()
tinhtong(s)