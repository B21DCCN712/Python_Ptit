s= input()

s1=0 # vietthuong
s2=0 # chuhoa
for i in s :
    if( i >='a' and i <='z') : s1+=1
    else: s2+=1
if s1 >= s2 : 
    s=s.lower()
    print(s)
else:
    s=s.upper()
    print(s)

    
