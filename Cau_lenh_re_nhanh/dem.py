s = input()
n=len(s)
i=0
dem1=0
dem2=0

for i in range(0,n):
    if s[i].isalpha: 
        dem1 +=1
    elif s[i].isdigit:
        while s[i].isdigist:
            i += 1
        dem2 +=1
print("so chu cai: " + str(dem1))
print("so chu so: " + str(dem2))