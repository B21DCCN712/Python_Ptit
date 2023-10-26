file = open("CONTACT.in",'r')
s=set()

for x in file:
    if x[-1]=='\n':
        x = x[:-1]
    s.add(x.lower())
s=sorted(s)
for x in s:
    print(x)
