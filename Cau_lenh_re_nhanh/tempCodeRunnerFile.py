s = input()
n=len(s)
i=0
dem1=0
dem2=0

while(i<n):
    if s[i].isalpha: 
        dem1 +=1
    elif s[i].isnumeric:
        while s[i].isnumeric:
            i += 1
        dem2 +=1
print("so chu cai: " + str(dem1))
print("so chu so: " + str(dem2))